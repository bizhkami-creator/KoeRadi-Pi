def parse_command(text):
    text = text.strip()

    if text in ["q", "exit", "quit", "終了"]:
        return "exit", None

    if text in ["s", "stop", "停止", "止めて", "ストップ"]:
        return "stop", None

    if "TBS" in text or "TBSラジオ" in text:
        return "play", "TBS"

    if "文化放送" in text or "QRR" in text:
        return "play", "QRR"

    if "ニッポン放送" in text or "LFR" in text:
        return "play", "LFR"

    if "TOKYO FM" in text or "東京FM" in text or "FMT" in text:
        return "play", "FMT"

    return "unknown", None
