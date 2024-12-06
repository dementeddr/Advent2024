#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 3 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    mul_pat = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    total = 0

    for line in data:
        matches = mul_pat.findall(line)
        
        for match in matches:
            print(match)
            total += int(match[0]) * int(match[1])

    print(total)


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

