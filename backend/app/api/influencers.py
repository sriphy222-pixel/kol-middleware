from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.influencer import Influencer
from app.schemas.influencer import InfluencerCreate, Influencer as InfluencerSchema

router = APIRouter()

@router.post("/", response_model=InfluencerSchema, status_code=status.HTTP_201_CREATED)
def create_influencer(influencer: InfluencerCreate, db: Session = Depends(get_db)):
    db_influencer = Influencer(**influencer.dict())
    db.add(db_influencer)
    db.commit()
    db.refresh(db_influencer)
    return db_influencer

@router.get("/", response_model=List[InfluencerSchema])
def read_influencers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    influencers = db.query(Influencer).offset(skip).limit(limit).all()
    return influencers

@router.get("/{influencer_id}", response_model=InfluencerSchema)
def read_influencer(influencer_id: int, db: Session = Depends(get_db)):
    db_influencer = db.query(Influencer).filter(Influencer.id == influencer_id).first()
    if db_influencer is None:
        raise HTTPException(status_code=404, detail="Influencer not found")
    return db_influencer
