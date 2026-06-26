from audio.recorder import record
from controller.command_parser import parse_command
from radiko.live_player import stop
from services.radio_service import RadioService
from voice.vosk_stt import transcribe



def main():
    print("==========================")
    print("   KoeRadi Pi Voice Mode")
    print("==========================")

    radio = RadioService()

    while True:
        input("Enterで録音開始...")

        audio_file = record(duration=3)
        text = transcribe(audio_file)

        print(f"認識結果: {text}")

        action, target = parse_command(text)

        if action == "exit":
            stop()
            print("Bye!")
            break

        if action == "stop":
            stop()
            continue

        if action == "play":
            print(f"▶ {target} を再生します")
            radio.play_live(target)
            continue

        print("コマンドを認識できませんでした。")


if __name__ == "__main__":
    main()
