# Backend for AI Assistant - Railway Deployment

This is the backend for the AI Assistant application, designed for deployment on Railway.

## Features

- FastAPI-based REST API
- Integration with Qdrant vector database
- Support for Gemini and Cohere AI models
- Automatic document ingestion
- CORS configured for Vercel frontend

## Environment Variables Required

The following environment variables must be set for the application to run:

```
GEMINI_API_KEY=your_google_gemini_api_key
COHERE_API_KEY=your_cohere_api_key
QDRANT_URL=your_qdrant_cluster_url
QDRANT_API_KEY=your_qdrant_api_key
```

Optional environment variables:
```
COLLECTION_NAME=curriculum_chunks (default)
CHUNK_MAX_CHARS=1200 (default)
SEARCH_TOP_K=5 (default)
MAX_TOKENS_RESPONSE=500 (default)
TEMPERATURE=0.3 (default)
```

## Health Check Endpoint

The application provides a health check endpoint:
- GET `/health` - Returns the health status of the service

Response format:
```json
{
  "status": "ok",
  "service": "railway-backend",
  "errors": false
}
```

## API Endpoints

- GET `/` - Root endpoint
- GET `/health` - Health check
- POST `/chat` - Chat endpoint
- POST `/admin/ingest` - Manual document ingestion
- GET `/admin/status` - Status of the Qdrant collection
- GET `/debug/docs` - Debug endpoint for docs directory

## Railway Deployment Notes

- The application listens on the port specified by the `PORT` environment variable
- CORS is configured to allow requests from `https://*.vercel.app`
- The startup process includes automatic document ingestion if the Qdrant collection is empty
- The application is built using the provided Dockerfile