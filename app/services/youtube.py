import yt_dlp
import subprocess

from app.services.asl_model import map_text_to_asl
from app.services.audio_processing import extract_audio_from_url
from app.services.text_processing import audio_to_text

MAX_VIDEO_DURATION = 60

def get_video_duration(url):
    """
    Get the duration of a video using yt-dlp or ffprobe.
    """
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "noplaylist": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("duration", 0)

def process_youtube_link_audio_only(url: str):
    """
    Process the YouTube video only if it meets the duration limit.
    """
    duration = get_video_duration(url)
    
    if duration > MAX_VIDEO_DURATION:
        return {
            "error": f"Video exceeds the maximum allowed duration of {MAX_VIDEO_DURATION} seconds. "
                     f"Current video length is {duration} seconds."
        }

    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "noplaylist": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info["url"]

    audio_data = extract_audio_from_url(audio_url)
    text = audio_to_text(audio_data)

    gestures = map_text_to_asl(text)

    return {"text": text, "gestures": gestures}
