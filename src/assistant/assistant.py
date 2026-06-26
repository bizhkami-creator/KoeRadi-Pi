from audio.recorder import record
from audio.player import play_wav
from ai.gemini_live_audio_client import ask_live_audio


class Assistant:
    def __init__(self):
        self.running = True

    def start(self):
        print("==========================")
        print(" KoeRadi AI Speaker")
        print("==========================")
        print("Enterで録音開始。Ctrl+Cで終了。")

        while self.running:
            input("\nEnterで話す...")

            audio_file = record(
                filename="sounds/assistant_input.wav",
                duration=3,
            )

            reply_wav = ask_live_audio(audio_file)
            play_wav(reply_wav)
