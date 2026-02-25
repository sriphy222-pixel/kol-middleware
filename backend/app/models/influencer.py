from sqlalchemy import Column, Integer, String, Float, JSON
from app.database import Base

class Influencer(Base):
    __tablename__ = "influencers"

    id = Column(Integer, primary_key=True, index=True)
    handle = Column(String, index=True, nullable=False)
    platform = Column(String, nullable=False)  # tiktok, instagram, youtube
    category = Column(String, nullable=True)
    follower_count = Column(Integer, nullable=True)
    engagement_rate = Column(Float, nullable=True)
    email = Column(String, nullable=True)
    status = Column(String, default="active")  # active, blacklisted
    tags = Column(JSON, nullable=True)  # Store tags as JSON array
