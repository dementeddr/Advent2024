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
    cur_pos = 0
    checksum = 0
    block_queue = deque()
    space_queue = deque()

    end = {}

    print(f"{len(line)} -> {end_id}")

    for i in range(0, len(line)-1, 2):

        s_file = int(line[i])
        s_space = int(line[i+1])

        e_file = int(line[-i-1])
        e_space = -1 if i == 0 else int(line[-i])
        
        print(f"{i} [{start_id}:{end_id}]: {s_file} {s_space}, {e_file} {e_space} | {cur_pos} {checksum}")

        for _ in range(s_file):
            checksum += cur_pos * start_id
            end[cur_pos] = hex(start_id)[-1]
            print(f"  s_file: {cur_pos} * {start_id} = {checksum}")
            cur_pos += 1

        if i <= max_id:
            for _ in range(e_file):
                print(f"  e_file: block in {end_id}")
                block_queue.append(end_id)

        for _ in range(s_space):
            print(f"  s_spac: space in {cur_pos}")
            space_queue.append(cur_pos)
            cur_pos += 1
        
        for _ in range(min(s_space, len(block_queue), len(space_queue))):
            block = block_queue.popleft()
            space = space_queue.popleft()
            checksum += block * space
            end[space] = hex(block)[-1]
            print(f"  queues: {block} * {space} = {checksum}")

        start_id += 1
        end_id -= 1
        print()

        if i > max_id and len(block_queue) == 0:
            break

    print(f"{max_id} [5]: {line[max_id]} | {cur_pos} {checksum}")

    '''
    for _ in range(int(line[max_id])):
        checksum += cur_pos * start_id
        end[cur_pos] = hex(start_id)[-1]
        print(f"center: {cur_pos} * {start_id} = {checksum}")
        cur_pos += 1
    '''
    '''
    for i in range(max_id, len(line), 2):
        
        s_file = int(line[i])
        s_space = int(line[i+1])

        for _ in range(s_space):

            if len(block_queue) == 0:
                break

            block = block_queue.popleft()
            checksum += block * cur_pos
            print(f"end-queue: {cur_pos} * {block} = {checksum}")
            end[cur_pos] = hex(block)[-1]
            cur_pos += 1

        if len(block_queue) == 0:
            break
    '''
    for i in sorted(end):
        print(end[i], end='')

    print()
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

