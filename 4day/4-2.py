#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 4 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    dirs = [(1,-1), (1,1), (-1,1), (-1,-1)]
    string = "MAS"
    count = 0
    
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1):
            mas_found = False
            for (i, direct) in enumerate(dirs):
                m_coord = (x-direct[0], y-direct[1])
                if data[y][x] != string[1]:
                    continue 
                res = search_dir(data, m_coord, direct, string)

                if res and mas_found:
                    count += 1
                elif res:
                    mas_found = True
                    
    print(count)


def search_dir(grid, coord, direct, string):

    if grid[coord[1]][coord[0]] != string[0]:
        return False

    for i in range(1, len(string)):
        nc = (coord[0] + i * direct[0], coord[1] + i * direct[1])
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

