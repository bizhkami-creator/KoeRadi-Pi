import xml.etree.ElementTree as ET
from urllib.request import urlopen


def get_weekly_programs(station_id="TBS"):
    url = f"https://radiko.jp/v3/program/station/weekly/{station_id}.xml"

    with urlopen(url) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)

    programs = []

    for prog in root.iter("prog"):
        title = prog.findtext("title")
        info = prog.findtext("info")
        pfm = prog.findtext("pfm")

        programs.append({
            "station_id": station_id,
            "title": title or "",
            "info": info or "",
            "pfm": pfm or "",
            "ft": prog.attrib.get("ft", ""),
            "to": prog.attrib.get("to", ""),
        })

    return programs


def search_program(station_id="TBS", keyword="安住"):
    programs = get_weekly_programs(station_id)

    results = []

    for p in programs:
        text = f"{p['title']} {p['info']} {p['pfm']}"
        if keyword in text:
            results.append(p)

    return results


if __name__ == "__main__":
    results = search_program("TBS", "安住")

    for i, p in enumerate(results, start=1):
        print(f"{i}. {p['title']}")
        print(f"   {p['ft']} - {p['to']}")
        print(f"   {p['pfm']}")
        print()
