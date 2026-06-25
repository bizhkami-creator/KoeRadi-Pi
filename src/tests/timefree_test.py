from radiko.programs import search_program
from radiko.timefree import play_timefree

program = search_program("TBS", "安住")[0]

print(program)

play_timefree(
    program["station_id"],
    program["ft"],
    program["to"],
)

input("Press Enter to stop...")
