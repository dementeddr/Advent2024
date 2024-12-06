#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 3 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    op_pat = re.compile(r"(?:do(?:n't)?|mul)\([0-9,]{0,7}\)")
    mul_pat = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    total = 0
    isEnabled = True

    for line in data:
        for op in map(lambda op: op[0], op_pat.finditer(line)):
            if op == "do()":
                isEnabled = True
            elif op == "don't()":
                isEnabled = False
            elif isEnabled:
                mul = mul_pat.match(op)
                total += int(mul.group(1)) * int(mul.group(2))
            
            print(f"{op}  -> {total} {isEnabled}")

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

