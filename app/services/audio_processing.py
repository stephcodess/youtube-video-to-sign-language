import requests
import ffmpeg

def extract_audio_from_url(audio_url: str):
    response = requests.get(audio_url, stream=True)
    if response.status_code != 200:
        raise Exception("Failed to fetch audio stream")

    # Process the audio stream using ffmpeg
    process = (
        ffmpeg.input("pipe:0")
        .output("pipe:1", format="wav", acodec="pcm_s16le")
        .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True)
    )
    audio_output, _ = process.communicate(input=response.content)
    return audio_output
