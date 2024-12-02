#!/usr/bin/python3

import sys
import copy
from time import perf_counter_ns

_day = 2 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    safe_count = 0

    for line in data:

        levels = list(map(lambda l: int(l), line.split(" ")))
        bad_count = 0

        if check_levels(levels):
            print (f"{line}  all good")
            safe_count += 1
            continue

        is_basically_safe = False

        for i in range(len(levels)):

            test_levels = copy.deepcopy(levels)
            del test_levels[i]

            is_basically_safe = check_levels(test_levels)

            if is_basically_safe:
                break

        print (f"{line}  basically_safe {is_basically_safe}")

        if is_basically_safe:
            safe_count += 1

    print(safe_count)


def check_levels(levels):
    prev_lev = -1
    direction = 0
    is_safe = True

    for lev in levels:

        if prev_lev == -1:
            prev_lev = lev
            continue

        diff = lev - prev_lev

        if diff >= 0 and direction < 0 or diff <= 0 and direction > 0 or abs(diff) < 1 or abs(diff) > 3:
            is_safe = False
            break

        direction = diff
        prev_lev = lev

    return is_safe

    
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

