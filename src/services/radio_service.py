from radiko.live_player import play_station
from radiko.programs import get_current_program


class RadioService:

    def play_live(self, station_id):

        current = get_current_program(station_id)

        if current:
            print(f"\n現在は『{current['title']}』を放送中です。")
            print(f"出演：{current['pfm']}\n")

        play_station(station_id)
