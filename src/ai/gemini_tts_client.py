import asyncio
import os
import wave

from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = "gemini-3.1-flash-live-preview"
OUTPUT_WAV = "sounds/assistant_reply.wav"


async def generate_voice_async(text):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    config = {
        "response_modalities": ["AUDIO"],
        "output_audio_transcription": {},
    }

    audio_chunks = []

    async with client.aio.live.connect(model=MODEL, config=config) as session:
        await session.send_realtime_input(text=text)

        async for response in session.receive():
            if response.server_content:
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

    return OUTPUT_WAV


def generate_voice(text):
    return asyncio.run(generate_voice_async(text))
