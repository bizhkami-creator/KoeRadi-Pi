PROGRAMS = [
    {
        "keywords": ["安住", "安住さん", "日曜天国", "にちてん"],
        "station": "TBS",
        "program": "安住紳一郎の日曜天国",
    },
    {
        "keywords": ["ジェーンスー", "ジェーン・スー", "生活は踊る"],
        "station": "TBS",
        "program": "ジェーン・スー 生活は踊る",
    },
    {
        "keywords": ["オードリー", "ANN", "オールナイトニッポン"],
        "station": "LFR",
        "program": "オードリーのオールナイトニッポン",
    },
    {
        "keywords": ["伊集院"],
        "station": "TBS",
        "program": "伊集院光とらじおと",
    },
]


def find_program(text):
    text = text.upper()

    for program in PROGRAMS:
        for keyword in program["keywords"]:
            if keyword.upper() in text:
                return program

    return None
