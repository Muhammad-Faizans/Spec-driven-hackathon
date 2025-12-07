from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from .database import SessionLocal, Base, engine, database_available
from .schemas import ContentChunk, ChatHistory # Import models
from .models import GeneralQueryRequest, GeneralQueryResponse, QueryResponseSource, SelectedTextQueryRequest, SelectedTextQueryResponse # Import Pydantic models
from .services.qdrant_service import QdrantService # Assuming QdrantService class is available
from .services.openai_service import OpenAIservice # Assuming OpenAIservice class is available

# Ensure all tables are created if database is available
if database_available and Base is not None:
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Could not create database tables: {e}")

app = FastAPI()

# Add CORS middleware to allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services with error handling
try:
    openai_service = OpenAIservice(api_key=os.getenv("OPENAI_API_KEY"))
    openai_available = True
except Exception as e:
    print(f"OpenAI service initialization failed: {e}")
    openai_service = None
    openai_available = False

try:
    qdrant_service = QdrantService(
        host=os.getenv("QDRANT_HOST", "localhost"),
        port=int(os.getenv("QDRANT_PORT", 6333)),
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name="book_content_chunks"
    )
    qdrant_available = True
except Exception as e:
    print(f"Qdrant service initialization failed: {e}")
    qdrant_service = None
    qdrant_available = False



@app.get("/")
def read_root():
    return {
        "message": "RAG Chatbot API is running!",
        "openai_available": openai_available,
        "qdrant_available": qdrant_available,
        "database_available": database_available
    }

@app.post("/query/general", response_model=GeneralQueryResponse)
async def query_general(request: GeneralQueryRequest):
    try:
        if not openai_available:
            raise HTTPException(status_code=503, detail="OpenAI service is not available. Please check your API key.")
        
        # If Qdrant is not available, use direct OpenAI response
        if not qdrant_available:
            prompt_for_llm = f"You are an expert in Physical AI and Humanoid Robotics. Answer the following question: {request.question}"
            response_from_llm = openai_service.generate_text(prompt_for_llm)
            return GeneralQueryResponse(answer=response_from_llm, sources=[])
        
        # Basic check for off-topic questions (heuristic)
        off_topic_keywords = ["weather", "time", "date"]
        if any(keyword in request.question.lower() for keyword in off_topic_keywords):
            return GeneralQueryResponse(answer="I can only answer questions related to Physical AI and Humanoid Robotics.", sources=[])

        # T016: Retrieve relevant text chunks from Qdrant and Postgres
        query_embedding = openai_service.get_embedding(request.question)
        if not query_embedding:
            raise HTTPException(status_code=500, detail="Failed to get embedding for the query.")

        search_result = qdrant_service.search(
            query_vector=query_embedding,
            limit=3 # Get top 3 most relevant chunks
        )

        relevant_chunks = []
        if search_result.hits:
            for hit in search_result.hits:
                relevant_chunks.append({
                    "content": hit.payload.get("content", "N/A"),
                    "source_location": hit.payload.get("source_location", "N/A")
                })
        
        # T024: If no relevant chunks are found, use general knowledge
        if not relevant_chunks:
            prompt_for_llm = f"You are an expert in Physical AI and Humanoid Robotics. Answer the following question: {request.question}"
            response_from_llm = openai_service.generate_text(prompt_for_llm)
            return GeneralQueryResponse(answer=response_from_llm, sources=[])
        
        # T017: Generate a final answer using the OpenAI API
        context_text = " ".join([f"{chunk['content']} (Source: {chunk['source_location']})\n" for chunk in relevant_chunks])
        
        prompt_for_llm = f"Based on the following context, answer the question: \n\nContext:\n{context_text}\n\nQuestion: {request.question}"

        response_from_llm = openai_service.generate_text(prompt_for_llm)

        # Format the response
        formatted_sources = [QueryResponseSource(source_location=chunk['source_location']) for chunk in relevant_chunks]
        
        return GeneralQueryResponse(answer=response_from_llm, sources=formatted_sources)

    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"An error occurred in query_general: {e}") # Log the error for debugging
        raise HTTPException(status_code=500, detail=f"An internal server error occurred: {str(e)}")


@app.post("/query/selected-text", response_model=SelectedTextQueryResponse)
async def query_selected_text(request: SelectedTextQueryRequest):
    try:
        if not openai_available:
            raise HTTPException(status_code=503, detail="OpenAI service is not available. Please check your API key.")
        
        # T015: Generate an answer using the OpenAI API, strictly using the selected text
        prompt_for_llm = f"You are an assistant that explains text snippets. Based ONLY on the following text, answer the user's question. If the answer is not present in the text, state that you cannot answer based on the provided information.\n\nProvided Text:\n{request.selected_text}\n\nQuestion: {request.question}"

        response_from_llm = openai_service.generate_text(prompt_for_llm)
        
        return SelectedTextQueryResponse(answer=response_from_llm, sources=[])

    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"An error occurred in query_selected_text: {e}") # Log the error for debugging
        raise HTTPException(status_code=500, detail=f"An internal server error occurred during selected text query: {str(e)}")

# Task T013 and T014 are conceptually covered by initializing the services above.
# Task T015 is the definition of this endpoint.
# Tasks T016 and T017 are implemented within this endpoint's logic.