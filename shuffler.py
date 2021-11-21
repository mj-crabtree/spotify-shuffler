#!/bin/python3
# shuffler.py
"""feed this script a text file with spotify tracks and it'll spit out a randomised tracklist"""

import sys
import random as rand


def file_check(file_path):
    line_count = 0
    test_string = 'https://open.spotify.com/track/'
    with open(file_path) as file:
        for line in file:
            track_id = line[-22:].strip()
            line_count += 1
            if line.lower().startswith(test_string) and track_id.isalnum():
                pass
            else:
                raise Exception(
                    f'error, line {str(line_count)}: "{line}" unsupported')


def read_tracklist(file_path):
    tracklist = []
    with open(file_path) as file:
        for line in file:
            tracklist.append(line.strip())
    return tracklist


def write_tracklist(tracklist, filename):
    rand.shuffle(tracklist)
    with open(filename, 'w') as file:
        for track in tracklist:
            file.write(f'{track}\n')


file_path = sys.argv[1]

try:
    file_check(file_path)
except Exception as ex:
    print(ex)
    exit()

tracklist = read_tracklist(file_path)
write_tracklist(tracklist, file_path)
