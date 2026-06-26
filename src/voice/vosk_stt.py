import json
import wave

from vosk import Model, KaldiRecognizer

MODEL_PATH = "models/vosk-model-small-ja-0.22"


def transcribe(audio_file):
    model = Model(MODEL_PATH)

    wf = wave.open(audio_file, "rb")

    recognizer = KaldiRecognizer(model, wf.getframerate())

    result_text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            result_text += result.get("text", "")

    final_result = json.loads(recognizer.FinalResult())
    result_text += final_result.get("text", "")

    return result_text.strip()
