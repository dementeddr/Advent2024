#!/usr/bin/python3

import sys
import re
import math
from collections import deque
from time import perf_counter_ns

_day = 9 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    line = data[0].strip()
    max_id = math.ceil(len(line)/2)-1
    start_id = 0
    end_id = max_id
    end_pos = len(line) - 1
    cur_pos = 0
    end_block = int(line[-1])
    checksum = 0
    space_queue = deque()

    output = {}

    print(f"{len(line)} -> {end_id}")
    print()

    for i in range(0, len(line)-1, 2):

        if i >= end_pos:
            break

        s_file = int(line[i])
        s_space = int(line[i+1])

        print(f"[{i} -> {start_id}]: {s_file} {s_space} | {cur_pos} {checksum}")

        for _ in range(s_file):
            checksum += cur_pos * start_id
            output[cur_pos] = hex(start_id)[-1]
            print(f"  s_file: {cur_pos} * {start_id} = {checksum}")
            cur_pos += 1

        for _ in range(s_space):
            print(f"  s_spac: space at {cur_pos}")
            space_queue.append(cur_pos)
            cur_pos += 1

        while len(space_queue) > 0 and i < end_pos:
            if end_block == 0:
                end_pos -= 2
                end_id -= 1
                if i>= end_pos:
                    break
                e_file = int(line[end_pos])
                end_block = e_file
                print(f"  e_file: moved to file {end_id} of length {e_file}")

            space = space_queue.popleft()
            checksum += end_id * space
            end_block -= 1
            output[space] = hex(end_id)[-1]
            print(f"  filled: [{end_block}] -> {space} * {end_id} = {checksum}")
        
        start_id += 1
        print()

    while end_block > 0:
        checksum += end_id * cur_pos
        print(f"finish end file: {end_id} * {cur_pos} = {checksum}")
        output[cur_pos] = hex(end_id)[-1]
        cur_pos += 1
        end_block -= 1

    #print()
    #keys = sorted(output)
    #out = ''

    #for i in range(keys[-1]+1):
    #    out += output[i] if i in keys else '.'

    #print(out)
    #print()
    print(f"Checksum = {checksum}")

    
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

