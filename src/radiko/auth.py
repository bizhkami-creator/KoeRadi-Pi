import base64
import re
import requests

AUTH1_URL = "https://radiko.jp/v2/api/auth1"
AUTH2_URL = "https://radiko.jp/v2/api/auth2"

JS_URLS = [
    "https://radiko.jp/apps/js/radikoJSPlayer.js",
    "https://radiko.jp/apps/js/playerCommon.js",
]

APP_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "X-Radiko-App": "pc_html5",
    "X-Radiko-App-Version": "0.0.1",
    "X-Radiko-User": "dummy_user",
    "X-Radiko-Device": "pc",
}


def find_auth_key():
    patterns = [
        r'authkey\s*[:=]\s*["\']([^"\']+)["\']',
        r'AUTH_KEY\s*[:=]\s*["\']([^"\']+)["\']',
        r'partialkey.*?["\']([A-Za-z0-9+/=]{40,})["\']',
        r'["\']([A-Za-z0-9+/=]{40,})["\']',
    ]

    for url in JS_URLS:
        print(f"Checking JS: {url}")
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        r.raise_for_status()
        text = r.text

        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                key = match.group(1)
                if len(key) >= 40:
                    print("Auth key found.")
                    return key

    raise RuntimeError("Auth key not found in radiko JS files.")


def get_auth_token():
    auth_key = find_auth_key()

    r = requests.get(AUTH1_URL, headers=APP_HEADERS, timeout=10)
    r.raise_for_status()

    auth_token = r.headers["X-Radiko-AuthToken"]
    key_offset = int(r.headers["X-Radiko-KeyOffset"])
    key_length = int(r.headers["X-Radiko-KeyLength"])

    partial_key_src = auth_key[key_offset:key_offset + key_length]
    partial_key = base64.b64encode(partial_key_src.encode("utf-8")).decode("utf-8")

    headers = {
        **APP_HEADERS,
        "X-Radiko-AuthToken": auth_token,
        "X-Radiko-PartialKey": partial_key,
    }

    r = requests.get(AUTH2_URL, headers=headers, timeout=10)

    print("auth2 status:", r.status_code)
    print("auth2 body:", r.text[:200])

    r.raise_for_status()

    return auth_token


if __name__ == "__main__":
    token = get_auth_token()
    print("Auth token:")
    print(token)

