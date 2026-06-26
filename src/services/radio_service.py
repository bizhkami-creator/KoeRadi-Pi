from radiko.live_player import play_station
from radiko.programs import get_current_program
from tts.speaker import speak


class RadioService:

    def play_live(self, station_id):
        current = get_current_program(station_id)

        if current:
            message = f"現在は、{current['title']}を放送中です。"
            print(f"\n{message}")
            print(f"出演：{current['pfm']}\n")
            speak(message)

        play_station(station_id)

