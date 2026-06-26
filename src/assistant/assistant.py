from audio.recorder import record
from conversation.conversation_service import ConversationService


class Assistant:
    def __init__(self):
        self.running = True
        self.conversation = ConversationService()

    def start(self):
        print("==========================")
        print(" KoeRadi AI Speaker")
        print("==========================")
        print("Enterで録音開始。Ctrl+Cで終了。")

        while self.running:
            input("\nEnterで話す...")

            audio_file = record(
                filename="sounds/assistant_input.wav",
                duration=5,
            )

            reply = self.conversation.chat_with_audio(audio_file)

            print("\nAI:")
            print(reply)

