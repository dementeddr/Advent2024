#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 6 #Advent of Code day

## BEGIN SOLUTION

dirs = [(0,-1), (1,0), (0,1), (-1,0)]
been = 'o'

def main(data):

    guard = (0,0)
    grid = []

    for y, line in enumerate(data):
        grid.append(list(line.strip()))
        if '^' in line:
            guard = (line.index('^'), y)

    step_count = 1
    face = 0
    
    while True:
        spot = check_dir(grid, guard, face)
        if spot == '#':
            face = (face + 1) % 4
        elif spot == '.':
            step_count += 1
            guard = add_coord(guard, dirs[face])
        elif spot == been or spot == '^':
            guard = add_coord(guard, dirs[face])
        elif spot == '':
            break
        else:
            raise ValueError(f"this isn't valid: {spot} at {guard}+{dirs[face]}")

        grid[guard[1]][guard[0]] = been

        #print(f"{step_count}  {face}")
    for line in grid:
        print(''.join(line))

        #input()

    print(f"\nStep Count = {step_count}")


def check_dir(grid, guard, face):
    try: 
        coord = add_coord(guard, dirs[face])
        return grid[coord[1]][coord[0]]

    except IndexError:
        return ''


def add_coord(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])


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

