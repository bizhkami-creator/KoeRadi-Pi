import os
from dotenv import load_dotenv
from google import genai

from audio.recorder import record

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def main():
    print("録音します。話してください。")

    audio_file = record(
        filename="sounds/gemini_input.wav",
        duration=5,
    )

    print("Geminiへ音声を送信します...")

    uploaded_file = client.files.upload(file=audio_file)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            uploaded_file,
            """
この音声の内容を理解して、日本語で自然に返事してください。
短く、やさしく、音声スピーカー向けに答えてください。
"""
        ],
    )

    print("\n=== Gemini Response ===")
    print(response.text)


if __name__ == "__main__":
    main()
