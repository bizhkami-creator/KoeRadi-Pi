from audio.recorder import record
from controller.command_parser import parse_command
from radiko.live_player import play_station, stop
from voice.stt import transcribe


def main():
    print("==========================")
    print("   KoeRadi Pi Voice Mode")
    print("==========================")

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
            play_station(target)
            continue

        print("コマンドを認識できませんでした。")


if __name__ == "__main__":
    main()
