# Research: RAG Chatbot Tech Stack

**Purpose**: To document the technology choices for the RAG chatbot feature, as outlined in the project constitution and feature specification.

## Decisions

### Backend Framework: FastAPI

-   **Decision**: Use FastAPI as the backend framework.
-   **Rationale**: FastAPI is a modern, high-performance Python web framework that is easy to learn and use. Its automatic OpenAPI documentation generation is ideal for creating clean, self-documenting APIs. It's well-suited for the asynchronous operations that will be involved in querying the database and language model.
-   **Alternatives Considered**:
    -   **Flask**: A solid choice, but lacks the built-in data validation and async support that FastAPI provides out-of-the-box.
    -   **Django**: Too large and complex for the scope of this project, which is primarily a single-purpose API.

### Vector Database: Qdrant Cloud

-   **Decision**: Use the Qdrant Cloud Free Tier.
-   **Rationale**: Qdrant is a high-performance vector search engine that is well-suited for RAG applications. The free tier is sufficient for the scope of this hackathon project. It has a straightforward Python client library.
-   **Alternatives Considered**:
    -   **Pinecone**: Another popular vector database, but Qdrant's free tier and open-source nature make it a good fit.
    -   **Local FAISS**: Could run a local vector index, but using a cloud service simplifies deployment and management.

### Relational Database: Neon Serverless Postgres

-   **Decision**: Use Neon Serverless Postgres.
-   **Rationale**: Neon provides a simple, serverless Postgres experience with a generous free tier. It's ideal for storing the text chunks and their metadata without requiring database management.
-   **Alternatives Considered**:
    -   **SQLite**: Simple to set up, but not ideal for a deployed web application.
    -   **Self-hosted Postgres**: Adds unnecessary operational overhead for this project.

### AI SDK: OpenAI

-   **Decision**: Use the OpenAI SDK.
-   **Rationale**: The specification explicitly requires the use of the OpenAI SDK. It is the standard for interacting with OpenAI's language models.
-   **Alternatives Considered**: None, as this was a requirement.
