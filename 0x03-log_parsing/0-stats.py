#!/usr/bin/env python3

"""
Reads stdin line by line and computes metrics.

Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size> (see input format above)

    Number of lines by status code:
    possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    format: <status code>: <number>
    status codes should be printed in ascending order
"""

import sys
from collections import defaultdict

total_size = 0
status_codes = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        try:
            ip, _, _, date, _, request, status_code, file_size = line.split()
            if request != 'GET /projects/260 HTTP/1.1':
                continue
            file_size = int(file_size)
            total_size += file_size
            status_codes[status_code] += 1
        except ValueError:
            continue

        if line_count == 10:
            print(f'Total file size: File size: {total_size}')
            for code in sorted(status_codes):
                print(f'{code}: {status_codes[code]}')
            print()

            line_count = 0
            status_codes = defaultdict(int)

except KeyboardInterrupt:
    print(f'Total file size: File size: {total_size}')
    for code in sorted(status_codes):
        print(f'{code}: {status_codes[code]}')

