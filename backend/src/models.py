from pydantic import BaseModel
from typing import List, Optional
import uuid

class QueryResponseSource(BaseModel):
    source_location: str

class GeneralQueryResponse(BaseModel):
    answer: str
    sources: List[QueryResponseSource]

class SelectedTextQueryResponse(BaseModel):
    answer: str
    sources: List[QueryResponseSource]

class GeneralQueryRequest(BaseModel):
    question: str

class SelectedTextQueryRequest(BaseModel):
    question: str
    selected_text: str
