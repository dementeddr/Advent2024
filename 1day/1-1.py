#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 1 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    list1 = []
    list2 = []
    
    for line in data:
        nums = line.split("  ")
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

    sort1 = sorted(list1)
    sort2 = sorted(list2)
    total_err = 0

    for i in range(len(sort1)):
        total_err += abs(sort1[i] - sort2[i])

    print(total_err)

    
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

