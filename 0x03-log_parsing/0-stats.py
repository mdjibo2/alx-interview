#!/usr/bin/python3

import sys
from collections import defaultdict

def print_msg(dict_sc, total_file_size):
    """
    Method to print statistics.
    Args:
        dict_sc: Dictionary of status codes and their counts.
        total_file_size: Total file size of the responses.
    Returns:
        Nothing.
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))

# defaultdict to count status codes
dict_sc = defaultdict(int)

# generator expression to sum file sizes
total_file_size = 0
for line in sys.stdin:
    try:
        total_file_size += int(line.split()[0])
    except ValueError:
        pass

# reset stdin
sys.stdin.seek(0)

# process input and count status codes
for line in sys.stdin:
    try:
        code = line.split()[1]
        dict_sc[code] += 1

        # print stats every 10 lines
        if dict_sc["200"] + dict_sc["301"] + dict_sc["400"] + dict_sc["401"] + dict_sc["403"] + dict_sc["404"] + dict_sc["405"] + dict_sc["500"] % 10 == 0:
            print_msg(dict_sc, total_file_size)
            dict_sc = defaultdict(int)

    except (ValueError, IndexError):
        pass

# print final stats
print_msg(dict_sc, total_file_size)
