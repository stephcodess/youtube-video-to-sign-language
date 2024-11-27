import speech_recognition as sr
from io import BytesIO

def audio_to_text(audio_data: bytes):
    recognizer = sr.Recognizer()
    audio_file = BytesIO(audio_data)
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
    return text
