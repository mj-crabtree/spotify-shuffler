#!python3
# shuffler.py

import random
import pyperclip as pc


def handle_input():
    tracklist = pc.paste()
    urls = tracklist.split("\n")
    random.shuffle(urls)
    return urls


def handle_output(tracklist):
    output = ""
    count = 0
    for track in tracklist:
        if not track.strip():
            continue
        else:
            output += track + "\n"
            count += 1
    print(f"successfully shuffled {count} tracks!")
    pc.copy(output)


def backup(data):
    with open(".backup", "w") as f:
        for line in data:
            f.write(line + "\n")


tracklist = handle_input()
handle_output(tracklist)
backup(tracklist)
