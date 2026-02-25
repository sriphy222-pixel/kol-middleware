from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.api.influencers import router as influencer_router
from app.api.auth import router as auth_router
from app.database import engine, Base, get_db
from app.models import influencer, user
from sqlalchemy.orm import Session
from app.core.security import get_password_hash

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
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])

@app.on_event("startup")
def create_default_user():
    db = next(get_db())
    admin = db.query(user.User).filter(user.User.username == "admin").first()
    if not admin:
        hashed_pwd = get_password_hash("admin123")
        new_admin = user.User(username="admin", email="admin@example.com", hashed_password=hashed_pwd, role="admin")
        db.add(new_admin)
        db.commit()
        print("Created default admin user: admin / admin123")

@app.get("/")
def read_root():
    return {"message": "Welcome to KOL Middleware API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
