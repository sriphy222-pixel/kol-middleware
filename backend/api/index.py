try:
    from app.main import app
except Exception as e:
    from fastapi import FastAPI
    app = FastAPI()
    
    @app.get("/")
    def error():
        return {"status": "error", "message": str(e), "type": type(e).__name__}

    @app.get("/{path:path}")
    def catch_all(path: str):
        return {"status": "error", "message": str(e), "type": type(e).__name__}
