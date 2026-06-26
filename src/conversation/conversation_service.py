from ai.gemini_audio_client import ask_gemini_audio


class ConversationService:
    def __init__(self):
        self.history = []

    def chat_with_audio(self, audio_file):
        reply = ask_gemini_audio(audio_file)

        self.history.append({
            "type": "audio",
            "file": audio_file,
            "reply": reply,
        })

        return reply
