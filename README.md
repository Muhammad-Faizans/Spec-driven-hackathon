# Physical AI & Humanoid Robotics Book

This is a comprehensive book on Physical AI and Humanoid Robotics featuring an integrated RAG chatbot, Urdu translation capabilities, and user authentication.

## Features

- **Integrated RAG Chatbot**: Ask questions about book content and get answers based only on the provided context
- **Urdu Translation**: Translate chapters to Urdu with preserved formatting
- **User Authentication**: Secure login/registration with user profile information
- **Selected Text Q&A**: Ask questions about specific text selections
- **Chat History**: Persistent conversation history per user

## Tech Stack

- **Frontend**: Docusaurus v3, React
- **Backend**: FastAPI, Python
- **Database**: PostgreSQL (Neon), SQLite (dev)
- **Vector Database**: Qdrant
- **AI Models**: OpenAI GPT-4o-mini
- **Authentication**: JWT-based authentication

## Prerequisites

- Node.js (v18+)
- Python (v3.8+)
- Docker (optional, for containerized deployment)

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Spec-driven-hackathon-1
```

### 2. Set up environment variables

Copy the example environment file and update the values:

```bash
cp .env.example .env
```

Update the `.env` file with your API keys and configuration:

- `GOOGLE_API_KEY`: Your Google API key for Gemini
- `QDRANT_API_KEY`: Your QDRANT API key (if using cloud)
- `QDRANT_HOST`: Qdrant endpoint (use 'localhost' for local development)
- `DATABASE_URL`: PostgreSQL connection string for Neon
- `SECRET_KEY`: A strong secret key for JWT

### 3. Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 4. Install frontend dependencies

```bash
cd ..  # Back to project root
yarn install
# or
npm install
```

## Running the Application

### Method 1: Development Mode (Separate Services)

**Terminal 1 - Start the backend:**
```bash
cd backend
python main.py
```

**Terminal 2 - Start the frontend:**
```bash
cd backend  # go back to project root
yarn start
# or
npm run start
```

### Method 2: Docker (Recommended for Production)

```bash
docker-compose up --build
```

The services will be available at:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Qdrant UI: http://localhost:6333

## Indexing Book Content

To index the book content for the RAG system, run:

```bash
python index_books.py
```

This will process all markdown files in the `docs` directory and store them in the vector database.

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/profile` - Get user profile
- `PUT /api/v1/auth/profile` - Update user profile

### RAG Chatbot
- `POST /api/v1/rag/chat` - Chat with the RAG system
- `GET /api/v1/rag/sessions` - Get user chat sessions
- `GET /api/v1/rag/sessions/{session_id}/messages` - Get session messages

### Translation
- `POST /api/v1/translate/translate` - Translate text
- `POST /api/v1/translate/translate-chapter` - Translate chapter preserving structure

## Folder Structure

```
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py         # Application entry point
│   │   ├── models/         # Database models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── routers/        # API routes
│   │   ├── services/       # Business logic
│   │   └── agents/         # AI agents and skills
├── docs/                   # Book content (markdown files)
├── src/                    # Docusaurus custom components
│   ├── components/         # React components
│   └── theme/              # Docusaurus theme overrides
├── scripts/                # Utility scripts
└── specs/                  # Requirements and specifications
```

## Environment Variables

Required environment variables:

```
GOOGLE_API_KEY=your_google_api_key_here
QDRANT_API_KEY=your_qdrant_api_key_here
QDRANT_HOST=your_qdrant_host_or_cluster_url
QDRANT_PORT=6333
DATABASE_URL=postgresql://user:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
SECRET_KEY=your-super-secret-and-very-long-key-change-this-in-production
FRONTEND_URL=http://localhost:3000
BACKEND_URL=http://localhost:8000
```

## Testing

To test the functionality of the services, run:

```bash
python test_functionality.py
```

## Deployment

For production deployment:

1. Use a production PostgreSQL database (like Neon)
2. Set up a Qdrant cloud instance
3. Configure proper domain names and SSL certificates
4. Update environment variables for production
5. Build and deploy using Docker or your preferred deployment method

## Troubleshooting

### Common Issues:

1. **API Keys**: Ensure all API keys are properly set in the `.env` file
2. **Database Connection**: Verify your database URL is correct
3. **Qdrant Connection**: Check that Qdrant is running and accessible
4. **CORS Issues**: If encountering CORS errors, update the CORS settings in `backend/app/main.py`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.