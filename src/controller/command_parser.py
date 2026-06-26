from data.programs import find_program

# ==========================================
# KoeRadi Pi Command Parser
# ==========================================

# -----------------------------
# Station aliases
# -----------------------------
STATION_ALIASES = {
    # TBS
    "1": "TBS",
    "TBS": "TBS",
    "TBSラジオ": "TBS",
    "TVS": "TBS",
    "TVSラジオ": "TBS",
    "PBS": "TBS",
    "PBSラジオ": "TBS",
    "ティービーエス": "TBS",
    "ティービーエスラジオ": "TBS",
    "キービーです": "TBS",
    "DBS": "TBS",
    "赤坂": "TBS",

    # 文化放送
    "2": "QRR",
    "QRR": "QRR",
    "文化放送": "QRR",

    # ニッポン放送
    "3": "LFR",
    "LFR": "LFR",
    "ニッポン放送": "LFR",
    "日本放送": "LFR",

    # TOKYO FM
    "4": "FMT",
    "FMT": "FMT",
    "TOKYO FM": "FMT",
    "TOKYOFM": "FMT",
    "東京FM": "FMT",
    "東京エフエム": "FMT",
}

# -----------------------------
# Stop / Exit
# -----------------------------
STOP_WORDS = [
    "止めて",
    "停止",
    "ストップ",
    "止まれ",
    "STOP",
]

EXIT_WORDS = [
    "終了",
    "終わり",
    "やめる",
    "EXIT",
    "QUIT",
]


def normalize_text(text: str) -> str:
    """
    Whisperの認識結果を検索しやすい形へ変換
    """
    return (
        text.strip()
        .replace("　", " ")
        .replace("。", "")
        .replace("、", "")
        .upper()
    )


def parse_command(text: str):
    text = normalize_text(text)

    if not text:
        return "unknown", None

    # -----------------------------
    # Exit
    # -----------------------------
    for word in EXIT_WORDS:
        if word.upper() in text:
            return "exit", None

    # -----------------------------
    # Stop
    # -----------------------------
    for word in STOP_WORDS:
        if word.upper() in text:
            return "stop", None

    # -----------------------------
    # Program / Personality Search
    # -----------------------------
    program = find_program(text)
    if program:
        return "play", program["station"]

    # -----------------------------
    # Station Search
    # -----------------------------
    for alias, station in STATION_ALIASES.items():
        if alias.upper() in text:
            return "play", station

    return "unknown", None
