import numpy as np
import sounddevice as sd
import soundfile as sf

DEVICE_ID = 1
OUTPUT_RATE = 48000

def play_wav(filename):
    data, samplerate = sf.read(filename, dtype="float32")

    if data.ndim > 1:
        data = data[:, 0]

    ratio = OUTPUT_RATE / samplerate
    new_length = int(len(data) * ratio)

    old_indices = np.arange(len(data))
    new_indices = np.linspace(0, len(data) - 1, new_length)

    data_resampled = np.interp(new_indices, old_indices, data).astype("float32")

    sd.play(data_resampled, samplerate=OUTPUT_RATE, device=DEVICE_ID)
    sd.wait()

