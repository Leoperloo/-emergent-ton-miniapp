from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ProjectCreate(BaseModel):
    title: str
    description: str
    funding_goal: float  # in TON
    entrepreneur_id: str

class Project(BaseModel):
    id: str
    title: str
    description: str
    funding_goal: float
    current_funding: float = 0.0
    status: str = "borrador"  # borrador, votacion, aprobado, fondeado
    entrepreneur_id: str
    likes: int = 0
    shares: int = 0
    comments_count: int = 0
    valuation: float = 0.0
    created_at: datetime
    voting_end: Optional[datetime] = None
