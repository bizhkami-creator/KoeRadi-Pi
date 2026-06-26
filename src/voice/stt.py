import subprocess

WHISPER_BIN = "/home/yocchan/whisper.cpp/build/bin/whisper-cli"
WHISPER_MODEL = "/home/yocchan/whisper.cpp/models/ggml-base.bin"


def transcribe(audio_file):
    result = subprocess.run(
        [
            WHISPER_BIN,
            "-m", WHISPER_MODEL,
            "-f", audio_file,
            "-l", "ja",
            "-nt",
        ],
        capture_output=True,
        text=True,
    )

    return result.stdout.strip()
