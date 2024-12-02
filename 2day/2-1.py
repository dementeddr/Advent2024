#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 2 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    safe_count = 0

    for line in data:

        levels = line.split(" ")
        prev_lev = -1
        direction = 0
        is_safe = True

        for lev in levels:
            level = int(lev)
            if prev_lev == -1:
                prev_lev = level
                continue

            diff = level - prev_lev

            if diff >= 0 and direction < 0  or diff <= 0 and direction > 0  or abs(diff) < 1 or abs(diff) > 3:
                is_safe = False
                break

            direction = diff
            prev_lev = level

        if is_safe:
            safe_count += 1

    print(safe_count)


    
## END SOLUTION

if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"
    data = []

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    with open(input_file, "r") as fp:
        data = fp.readlines()

    time_start = perf_counter_ns()
    main(data)
    time_stop = perf_counter_ns()

    time = (time_stop - time_start) / 1000000
    print(f"\nExecution took {time:.4f} milliseconds")

