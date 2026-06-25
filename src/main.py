from radiko.live_player import play_station, stop
import time


def main():
    print("======================")
    print(" KoeRadi Pi Day3")
    print("======================")

    play_station("TBS")

    print("Playing for 30 seconds...")
    time.sleep(30)

    stop()
    print("Done.")


if __name__ == "__main__":
    main()

