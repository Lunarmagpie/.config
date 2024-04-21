import subprocess
import json
import sys


def loop():
    msg = json.loads(
        subprocess.check_output(["swaymsg", "-r", "-t", "subscribe", '["window"]'])
    )

    width = msg["container"]["rect"]["width"]
    height = msg["container"]["rect"]["height"]

    if width >= height:
        subprocess.run(["swaymsg", "splith"])
    else:
        subprocess.run(["swaymsg", "splitv"])


def main():
    while True:
        try:
            loop()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
