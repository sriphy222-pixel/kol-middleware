from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.influencers import router as influencer_router
from app.database import engine, Base
from app.models import influencer

# Create tables if not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="KOL Connection Middleware API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(influencer_router, prefix="/api/v1/influencers", tags=["influencers"])

@app.get("/")
def read_root():
    return {"message": "Welcome to KOL Middleware API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
