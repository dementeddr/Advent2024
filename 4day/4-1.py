#!/usr/bin/python3
#pylint: disable=W

import sys
import re
from time import perf_counter_ns

_day = 4 #Advent of Code day

## BEGIN SOLUTION


def main(data):

    exes = []
    dirs = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]
    string = "XMAS"
    count = 0
    
    for y in range(len(data)):
        for x in range(len(data[y])):
            for d in dirs:
                if search_dir(data, (x,y), d[0], d[1], string):
                    count += 1
    print(count)

def search_dir(grid, coord, xdir, ydir, string):

    if grid[coord[1]][coord[0]] != string[0]:
        return False
    if ydir < 0 and coord[1] < 3: #up
        return False
    if ydir > 0 and coord[1] > len(grid) - 4: #down
        return False
    if xdir < 0 and coord[0] < 3: #left
        return False
    if xdir > 0 and coord[0] > len(grid[coord[1]]) - 4: #right
        return False

    for i in range(1, len(string)):
        nc = (coord[0] + i * xdir, coord[1] + i * ydir)
        if grid[nc[1]][nc[0]] != string[i]:
            return False
    
    return True


    
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

