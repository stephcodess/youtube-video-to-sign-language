from fastapi import APIRouter, Form
from app.services.youtube import process_youtube_link_audio_only

router = APIRouter()

@router.post("/process/")
async def process_youtube(url: str = Form(...)):
    result = process_youtube_link_audio_only(url)
    return result
