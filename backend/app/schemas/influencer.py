from pydantic import BaseModel, EmailStr
from typing import List, Optional

class InfluencerBase(BaseModel):
    handle: str
    platform: str
    category: Optional[str] = None
    follower_count: Optional[int] = 0
    engagement_rate: Optional[float] = 0.0
    email: Optional[EmailStr] = None
    tags: Optional[List[str]] = []

class InfluencerCreate(InfluencerBase):
    pass

class Influencer(InfluencerBase):
    id: int
    status: str

    class Config:
        from_attributes = True
