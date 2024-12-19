#!/usr/bin/python3

import sys
from time import perf_counter_ns

from trinary_counter import trinary_counter

_day = 7 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    calibration = 0

    for line in data:
        tokens = line.split(" ")
        result = int(tokens[0][:-1])
        nums = list(map(int, tokens[1:]))

        if assemble_ops(result, nums):
            calibration += result
    
        #input('\n')
    print(f"\nTotal Calibration Result = {calibration}")
        

def assemble_ops(result, vals):

    ops = ['-' for n in range(len(vals)-1)]

    def inner_ops(total, inums):
        if len(inums) == 0:
            return total == result

        i = len(vals) - len(inums) - 1
            
        for op in range(3):
            itotal = total
            if op == 0:
                itotal += inums[0]
                ops[i] = '+'
            elif op == 1:
                itotal *= inums[0]
                ops[i] = '*'
            else:
                #print(f"  {itotal} -> ", end='')
                itotal *= 10 ** len(str(inums[0]))
                #print(f"{len(str(inums[0]))} = {itotal}, +{inums[0]} = ", end='')
                itotal += inums[0]
                #print(itotal)
                ops[i] = '|'

            if inner_ops(itotal, inums[1:]):
                return True
        
        return False

    #return inner_ops(vals[0], vals[1:])
    if inner_ops(vals[0], vals[1:]):
        print("Success:", end='')
        print_eq(result, vals, ops)
        return True
    else:
        print(f"Failure: {result} != {vals}")
        return False


def print_eq(result, vals, ops):
    out = str(vals[0])
    for (val, op) in zip(vals[1:], ops):
        out += f" {op} {val}"
    print(f" {result} = {out}")


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

