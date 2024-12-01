#!/usr/bin/python3

import sys
import re
from collections import defaultdict
from time import perf_counter_ns

_day = 1 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    left_list = []
    right_reps = defaultdict(int)

    for line in data:
        nums = line.split("  ")
        left_list.append(int(nums[0]))
        right_reps[int(nums[1])] += 1

    similarity = 0

    for lefty in left_list:
        similarity += lefty * right_reps[lefty]

    print(similarity)

    
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

