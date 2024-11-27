from fastapi import FastAPI
from app.api import youtube, health

app = FastAPI()

app.include_router(youtube.router, prefix="/youtube", tags=["YouTube"])
app.include_router(health.router, prefix="/health", tags=["Health"])

@app.get("/")
def root():
    return {"message": "Welcome to the Deaf Accessibility App!"}
