import asyncio
import os
import wave

import numpy as np
import soundfile as sf
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

MODEL = "gemini-3.1-flash-live-preview"
OUTPUT_WAV = "sounds/live_reply.wav"


def wav_to_pcm16(audio_file):
    data, samplerate = sf.read(audio_file, dtype="float32")

    if data.ndim > 1:
        data = data[:, 0]

    # float32 -1.0〜1.0 → int16 PCM
    data = np.clip(data, -1.0, 1.0)
    pcm16 = (data * 32767).astype(np.int16)

    return pcm16.tobytes(), samplerate


async def ask_live_audio_async(audio_file):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    pcm_bytes, samplerate = wav_to_pcm16(audio_file)

    config = {
        "response_modalities": ["AUDIO"],
        "system_instruction": (
            "あなたは家庭用AIスピーカーです。"
            "日本語で短く、やさしく、自然に返答してください。"
        ),
    }

    audio_chunks = []

    async with client.aio.live.connect(model=MODEL, config=config) as session:
        await session.send_realtime_input(
            audio=types.Blob(
                data=pcm_bytes,
                mime_type=f"audio/pcm;rate={samplerate}",
            )
        )

        async for response in session.receive():
            if response.server_content and response.server_content.model_turn:
                for part in response.server_content.model_turn.parts:
                    if part.inline_data:
                        audio_chunks.append(part.inline_data.data)

            if response.server_content and response.server_content.turn_complete:
                break

    audio_data = b"".join(audio_chunks)

    with wave.open(OUTPUT_WAV, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(audio_data)

    return OUTPUT_WAV


def ask_live_audio(audio_file):
    return asyncio.run(ask_live_audio_async(audio_file))

