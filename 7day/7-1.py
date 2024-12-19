#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

from binary_counter import binary_counter

_day = 7 #Advent of Code day

## BEGIN SOLUTION


def main(data):

    calibration = 0

    for line in data:
        tokens = line.split(" ")
        result = int(tokens[0][:-1])
        nums = list(map(int, tokens[1:]))

        print(f"\n{result} = {nums}")

        for ops in range(2 ** (len(nums)-1)):
            total = assemble_ops(nums,  ops)
            if total == result:
                calibration += result
                print("Success!")
                break

    print(f"Total Calibration Result = {calibration}")
        

def assemble_ops(nums, ops):

    total = nums[0]
    ops_counter = binary_counter(ops)
    out = str(total)

    for (num, op_bit) in zip(nums[1:], ops_counter):
        #out+=f" {'*' if op_bit else '+'} {num}"

        if op_bit: #True = multiply, False = add
            total *= num
        else:
            total += num
    
    #print(f"{out} = {total}")
    return total

 
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

