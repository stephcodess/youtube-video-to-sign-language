from fastapi import APIRouter, UploadFile
from app.services.audio_processing import process_uploaded_video

router = APIRouter()

@router.post("/process/")
async def process_video(file: UploadFile):
    result = process_uploaded_video(file)
    return result
