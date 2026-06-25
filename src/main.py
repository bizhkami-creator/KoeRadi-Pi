from radiko.live_player import play_station, stop

STATIONS = {
    "1": ("TBS", "TBSラジオ"),
    "2": ("QRR", "文化放送"),
    "3": ("LFR", "ニッポン放送"),
    "4": ("FMT", "TOKYO FM"),
}


def show_menu():
    print("\n==========================")
    print("      KoeRadi Pi")
    print("==========================")
    print("1. TBSラジオ")
    print("2. 文化放送")
    print("3. ニッポン放送")
    print("4. TOKYO FM")
    print("--------------------------")
    print("s : Stop")
    print("q : Quit")
    print("==========================")


def main():
    while True:
        show_menu()

        cmd = input("> ").strip().lower()

        if cmd == "q":
            stop()
            print("Bye!")
            break

        if cmd == "s":
            stop()
            continue

        if cmd in STATIONS:
            station_id, name = STATIONS[cmd]
            print(f"\n▶ {name} を再生します\n")
            play_station(station_id)
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()

