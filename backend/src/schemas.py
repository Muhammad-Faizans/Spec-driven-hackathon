from sqlalchemy import Column, String, DateTime, Text, UUID
from sqlalchemy.sql import func
import uuid

from .database import Base

class ContentChunk(Base):
    __tablename__ = "content_chunks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text, nullable=False)
    source_location = Column(String, nullable=False)
    qdrant_vector_id = Column(UUID(as_uuid=True), nullable=True) # This would be linked to Qdrant's internal ID
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(String, nullable=False)
    query = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
