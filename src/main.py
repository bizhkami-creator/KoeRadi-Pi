from audio.recorder import record
from audio.player import play_wav

def main():
    print("======================")
    print(" KoeRadi Pi")
    print("======================")

    audio_file = record(duration=3)
    play_wav(audio_file)

    print("Done.")

if __name__ == "__main__":
    main()

