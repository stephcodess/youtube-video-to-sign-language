from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_video_process():
    with open("./app/temp/sample.mp4", "rb") as video:
        response = client.post("/video/process/", files={"file": ("sample.mp4", video, "video/mp4")})
    assert response.status_code == 200
    assert "audio_path" in response.json()
    assert "asl_gestures" in response.json()
