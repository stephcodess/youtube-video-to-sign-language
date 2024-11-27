from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_youtube_process():
    response = client.post("/youtube/process/", data={"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"})
    assert response.status_code == 200
    assert "video_path" in response.json()
    assert "audio_path" in response.json()
