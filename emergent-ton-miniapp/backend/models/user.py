from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    telegram_id: str
    wallet_address: Optional[str] = None
    roles: List[str] = ["donador"]  # emprendedor, donador, ballena
    diamonds: float = 0.0
    created_at: datetime = datetime.utcnow()
