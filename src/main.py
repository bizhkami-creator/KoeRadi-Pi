from controller.command_parser import parse_command
from radiko.live_player import play_station, stop


def show_menu():
    print("\n==========================")
    print("      KoeRadi Pi")
    print("==========================")
    print("例: TBS / 文化放送 / ニッポン放送 / TOKYO FM")
    print("例: 止めて / 終了")
    print("==========================")


def main():
    while True:
        show_menu()

        text = input("> ").strip()
        action, target = parse_command(text)

        if action == "exit":
            stop()
            print("Bye!")
            break

        if action == "stop":
            stop()
            continue

        if action == "play":
            print(f"\n▶ {target} を再生します\n")
            play_station(target)
            continue

        print("Unknown command")


if __name__ == "__main__":
    main()
