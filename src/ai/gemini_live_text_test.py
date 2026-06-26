import asyncio
import os
import wave

from dotenv import load_dotenv
from google import genai

from audio.player import play_wav

load_dotenv()

MODEL = "gemini-3.1-flash-live-preview"
OUTPUT_WAV = "sounds/gemini_live_response.wav"


async def main():
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    config = {
        "response_modalities": ["AUDIO"],
        "output_audio_transcription": {},
    }

    audio_chunks = []

    async with client.aio.live.connect(model=MODEL, config=config) as session:
        await session.send_realtime_input(
            text="こんにちは。あなたは高齢者向けのやさしいAIスピーカーです。短く日本語で挨拶してください。"
        )

        async for response in session.receive():
            if response.server_content:
                if response.server_content.output_transcription:
                    print("Transcript:", response.server_content.output_transcription.text)

                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_chunks.append(part.inline_data.data)

                if response.server_content.turn_complete:
                    break

    audio_data = b"".join(audio_chunks)

    with wave.open(OUTPUT_WAV, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(audio_data)

    print(f"Saved: {OUTPUT_WAV}")
    play_wav(OUTPUT_WAV)


if __name__ == "__main__":
    asyncio.run(main())
