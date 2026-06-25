import subprocess

from radiko.auth import get_auth_token

current_process = None


def build_timefree_url(station_id, ft, to):
    return (
        "https://tf-f-rpaa-radiko.smartstream.ne.jp/tf/playlist.m3u8"
        f"?station_id={station_id}"
        f"&ft={ft}"
        f"&to={to}"
        "&l=15"
        "&type=b"
    )


def play_timefree(station_id, ft, to):
    global current_process

    stop()

    token = get_auth_token()

    url = build_timefree_url(station_id, ft, to)

    print("Playing TimeFree")
    print(url)

    current_process = subprocess.Popen(
        [
            "mpv",
            "--no-video",
            f"--http-header-fields=X-Radiko-AuthToken: {token}",
            url,
        ]
    )


def stop():
    global current_process

    if current_process:
        current_process.terminate()
        current_process = None
