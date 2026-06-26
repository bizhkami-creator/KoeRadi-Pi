import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini_audio(audio_file):
    uploaded_file = client.files.upload(file=audio_file)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            uploaded_file,
            """
あなたは高齢者にもやさしいAIホームスピーカーです。
日本語で短く、自然に返事してください。
"""
        ],
    )

    return response.text.strip()

