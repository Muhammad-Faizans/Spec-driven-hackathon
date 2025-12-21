# Project Specification

## Tech Stack Overview

### Frontend
- **Framework**: Docusaurus v3.9.2 (React-based static site generator)
- **Language**: TypeScript
- **Styling**: Tailwind CSS (presumably, though not explicitly in package.json)
- **Build Tool**: Node.js (v20+)
- **Deployment**: Vercel

### Backend
- **Framework**: FastAPI (Python)
- **Language**: Python 3.8+
- **Vector Database**: Qdrant
- **AI Models**: Google Gemini, OpenAI, Cohere
- **Web Server**: Uvicorn (ASGI server)
- **Additional Libraries**: qdrant-client, google-generativeai, cohere, flask-cors

### Infrastructure
- **Containerization**: Docker (Dockerfile.backend, Dockerfile.frontend)
- **Orchestration**: Docker Compose
- **Deployment**: Vercel (frontend), Railway (backend based on railway.json)

## Folder Structure

```
project-root/
├── .specify/                 # Specification-driven development artifacts
│   └── memory/
│       └── constitution.md
├── backend/                  # Backend services (Python/FastAPI)
│   ├── app/                  # Main application code
│   ├── requirements.txt      # Python dependencies
│   ├── api.py                # Main API entry point
│   ├── api_flask.py          # Flask API alternative
│   ├── config.py             # Configuration management
│   ├── chat_gemini.py        # Gemini integration
│   ├── ingest_local_docs.py  # Document ingestion pipeline
│   └── ...
├── src/                      # Frontend source code
│   ├── components/           # React components
│   ├── css/                  # Stylesheets
│   ├── pages/                # Page components
│   └── theme/                # Theme customization
├── docs/                     # Documentation
├── blog/                     # Blog posts
├── specs/                    # Specifications
├── history/                  # Project history
├── scripts/                  # Utility scripts
├── static/                   # Static assets
├── .env.example              # Environment variables template
├── package.json              # Frontend dependencies
├── docker-compose.yml        # Docker orchestration
├── Dockerfile.backend        # Backend container
├── Dockerfile.frontend       # Frontend container
└── README.md                 # Project documentation
```

## Frontend Responsibilities

### Core Features
- Documentation website serving
- Interactive chat interface for RAG system
- Document upload and management UI
- Model selection interface
- Conversation history display

### Pages
- Home page with project overview
- Chat interface with streaming responses
- Document management page
- Settings/configuration page
- API status dashboard

### Components
- ChatMessage: Display individual messages with citations
- ChatInput: Handle user input and submission
- DocumentUpload: Drag-and-drop file upload
- ModelSelector: Dropdown for AI model selection
- LoadingSpinner: Visual feedback during processing

## Backend Responsibilities

### Core APIs
- `/chat`: Process chat requests with RAG context
- `/upload`: Handle document uploads and ingestion
- `/documents`: Manage stored documents
- `/models`: List available AI models
- `/collections`: Manage Qdrant collections
- `/health`: System health check

### RAG Pipeline
- Document ingestion from various formats (PDF, DOCX, TXT)
- Text preprocessing and normalization
- Embedding generation using AI models
- Vector storage in Qdrant database
- Semantic search and retrieval
- Context-aware response generation

### Configuration Management
- Environment variable validation
- API key management
- Database connection handling
- CORS policy enforcement

## RAG Flow

### 1. Data Ingestion
```
Document Upload → Format Validation → Text Extraction → Preprocessing → Chunking → Embedding Generation → Vector Storage
```

### 2. Query Processing
```
User Query → Embedding Generation → Vector Similarity Search → Context Retrieval → Response Generation → Response Formatting
```

### 3. Response Generation
```
Retrieved Context + User Query → Prompt Engineering → AI Model Call → Response Streaming → Citation Attachment
```

## Environment Variables

### Required Variables
- `QDRANT_API_KEY`: API key for Qdrant vector database
- `QDRANT_HOST`: Host URL for Qdrant cluster
- `QDRANT_PORT`: Port for Qdrant connection (default: 6333)
- `GOOGLE_API_KEY`: API key for Google Gemini
- `OPENAI_API_KEY`: API key for OpenAI services
- `COHERE_API_KEY`: API key for Cohere services

### Optional Variables
- `DATABASE_URL`: PostgreSQL connection string (for future use)
- `SECRET_KEY`: JWT secret for authentication
- `FRONTEND_URL`: Allowed origin for CORS
- `BACKEND_URL`: Backend URL for API calls
- `QDRANT_LOCAL_PATH`: Local path for Qdrant (for development)

## Deployment Targets

### Frontend (Vercel)
- Static site generation using Docusaurus
- CDN distribution for global access
- Automatic SSL certificate management
- Preview deployments for pull requests

### Backend (Railway)
- Containerized FastAPI application
- Auto-scaling based on demand
- Environment variable management
- Health check monitoring

### Database (Qdrant Cloud)
- Managed vector database service
- Auto-backup and recovery
- Horizontal scaling capabilities
- Security and access controls

## Security Considerations

### API Protection
- Rate limiting for API endpoints
- Authentication for sensitive operations
- Input validation and sanitization
- HTTPS enforcement

### Data Protection
- Encryption of sensitive data in transit
- Secure storage of API keys
- Access logging and monitoring
- Data retention policies

## Performance Requirements

### Response Times
- API calls: < 2 seconds for simple queries
- Chat responses: < 5 seconds for complex queries
- Document ingestion: < 30 seconds per document
- Search operations: < 1 second

### Concurrency
- Support for 100+ concurrent users
- Queue management for heavy operations
- Resource utilization monitoring
- Auto-scaling based on load

## Monitoring & Observability

### Logging
- Structured logging for all API calls
- Error tracking and alerting
- Performance metric collection
- Audit trail for user actions

### Metrics
- API response times
- Error rates and types
- Active user sessions
- Vector database performance
- Token usage by model