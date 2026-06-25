
import sounddevice as sd
import soundfile as sf

DEVICE_ID = 1
SAMPLE_RATE = 16000
CHANNELS = 1

def record(filename="sounds/input.wav", duration=3):
    print("Recording...")

    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32",
        device=DEVICE_ID,
    )

    sd.wait()
    sf.write(filename, audio, SAMPLE_RATE)

    print(f"Saved: {filename}")
    return filename

