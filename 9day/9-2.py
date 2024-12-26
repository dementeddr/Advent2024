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
    checksum = 0
    files = []
    spaces = []

    for i in range(0, len(line)-1, 2):
        file = int(line[i])
        space = [int(line[i+1]), []]
        files.append(file)
        spaces.append(space)

    files.append(int(line[-1]))

    for fid, file in reversed(list(enumerate(files))):
        if fid == 0:
            break
        print(f"Checking file {fid}, len {file}")
        for i, space in enumerate(spaces[:fid]):
            if space[0] >= file:
                print(f"  Moving fid {fid} to space {i} {space}")
                files[fid] = -file
                for _ in range(file):
                    space[1].append(fid)
                space[0] -= file
                break

    block_pos = 0
    out = ''
    print()

    for fid, (file, space) in enumerate(zip(files, spaces)):
        if file < 0:
            print(f"[{block_pos}] -> [{block_pos - file}], file moved.")
            block_pos -= file
            out += -file * '.'
        else:
            for _ in range(file):
                checksum += block_pos * fid
                print(f"[{block_pos}] * {fid} = {checksum}") 
                block_pos += 1
                out += str(fid)# + "'"

        for sfid in space[1]:
            checksum += block_pos * sfid
            print(f"[{block_pos}] * {sfid} = {checksum}") 
            block_pos += 1

        print(f"[{block_pos}] -> [{block_pos + space[0]}], space.")
        block_pos += space[0]

        out += format_space(space)

    print()
    print(out)
    print()
    print(f"Checksum = {checksum}")


def format_spaces(spaces):
    out_list = []
    for space in spaces:
        out_list.append(format_space(space))
    return out_list


def format_space(space):
    out_str = ''
    for block in space[1]:
        out_str += str(block)# + "'"
    out_str += '.' * space[0]
    return out_str

    
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

