import subprocess
import xml.etree.ElementTree as ET
from urllib.request import urlopen

STATIONS = {
    "TBS": "https://radiko.jp/v2/station/stream_smh_multi/TBS.xml",
    "QRR": "https://radiko.jp/v2/station/stream_smh_multi/QRR.xml",
    "LFR": "https://radiko.jp/v2/station/stream_smh_multi/LFR.xml",
    "FMT": "https://radiko.jp/v2/station/stream_smh_multi/FMT.xml",
}

current_process = None


def get_stream_url(station_id):
    xml_url = STATIONS.get(station_id)

    if not xml_url:
        raise ValueError(f"Unknown station: {station_id}")

    with urlopen(xml_url) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)

    for item in root.iter():
        if item.text and "m3u8" in item.text:
            return item.text.strip()

    raise ValueError(f"Stream URL not found for {station_id}")


def play_station(station_id="TBS"):
    global current_process

    stop()

    print(f"Getting stream URL: {station_id}")
    stream_url = get_stream_url(station_id)

    print(f"Playing station: {station_id}")
    print(stream_url)

    current_process = subprocess.Popen(
        ["mpv", "--no-video", stream_url]
    )


def stop():
    global current_process

    if current_process:
        print("Stopping...")
        current_process.terminate()
        current_process = None

