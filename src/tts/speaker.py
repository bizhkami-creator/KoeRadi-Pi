import subprocess


def speak(text):
    print(f"🔊 {text}")

    subprocess.run(
        [
            "espeak-ng",
            "-v",
            "ja",
            text,
        ],
        check=False,
    )
