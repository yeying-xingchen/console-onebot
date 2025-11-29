"""程序入口"""

import json
import sys
import tomllib
import requests

if __name__ == "__main__":
    with open("./test/config.toml", "rb") as f:
        config = tomllib.load(f)
    action = sys.argv[1]
    info = {}
    if action == "private_message":
        info = {
            "time": 1515204254,
            "self_id": 10001000,
            "post_type": "message",
            "message_type": "private",
            "sub_type": "friend",
            "message_id": 12,
            "user_id": sys.argv[3],
            "message": sys.argv[2],
            "raw_message": sys.argv[2],
            "font": 456,
            "sender": {
                "nickname": sys.argv[4],
                "sex": "male",
                "age": 18
            }
        }
    resp = requests.post(config["url"],json=info, timeout=10)
    reply = json.loads(resp.text)
    if reply["reply"] != sys.argv[5]:
        print("与预期回复不符")
