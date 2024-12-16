#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 6 #Advent of Code day

## BEGIN SOLUTION

dirs = [(0,-1), (1,0), (0,1), (-1,0)]
do_print = False

def main(data):

    global do_print
    guard = (0,0)
    grid = []

    for y, line in enumerate(data):
        grid.append(list(line.strip()))
        if '^' in line:
            guard = (line.index('^'), y)

    block_count = 0
    face = 0
    
    while True:
        grid[guard[1]][guard[0]] = str(face)
        spot = check_dir(grid, guard, face)

        if spot == '':
            break
        if spot == '#':
            face = (face + 1) % 4
        elif spot == '^':
            if face == 3:
                block_count += 1
            guard = add_coord(guard, dirs[face])

        elif spot.isdigit():
            guard = add_coord(guard, dirs[face])

        elif spot == '.':
            next_g = add_coord(guard, dirs[face])
            grid[next_g[1]][next_g[0]] = '#'
            if check_for_loop(grid, guard, face):
                block_count += 1
                #grid[guard[1]][guard[0]] = '@'
                #print_grid(grid)
                #grid[guard[1]][guard[0]] = str(face)
            guard = add_coord(guard, dirs[face])

        else:
            raise ValueError(f"this isn't valid: {spot} at {guard}+{dirs[face]}")

        if block_count >= 26:
            do_print = True

        #print(f"{block_count}  {spot}")
        #print_grid(grid)
        #input()

    print_grid(grid)
    print(f"\nBlock Count = {block_count}")


def check_dir(grid, guard, face):
    try: 
        coord = add_coord(guard, dirs[face])
        if coord[1] < 0 or coord[1] >= len(grid) or coord[0] < 0 or coord[0] >= len(grid[coord[1]]):
            return ''
        return grid[coord[1]][coord[0]]

    except IndexError:
        return ''


def check_for_loop(grid, guard, face):
    #grid = copy_grid(grood)
    ray_g = guard
    ray_face = (face + 1) % 4
    visited = {}

    while True:
        spot = check_dir(grid, ray_g, ray_face)

        if spot == '':
            return False
        if spot == '#':
            ray_face = (ray_face+1)%4
        elif spot == '.':
            if ray_g in visited and visited[ray_g] == ray_face:
                return True
            visited[ray_g] = ray_face
            ray_g = add_coord(ray_g, dirs[ray_face])
        elif spot.isdigit():
            if int(spot) == ray_face:
                return True
            visited[ray_g] = ray_face
            ray_g = add_coord(ray_g, dirs[ray_face])

        #print(f"{guard} {ray_g}")
        #print_grid(grid, replace_coord=ray_g, replace_with='%')
        #input()


def add_coord(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])


def print_grid(grid, replace_coord=None, replace_with=None):
    for y, line in enumerate(grid):
        out = ''
        for x, spot in enumerate(line):
            if replace_coord != None and replace_coord[0] == x and replace_coord[1] == y:
                out += replace_with
            else:
                out += spot
        print(out)
        
    print()

def copy_grid(grid):
    new_grid = []
    for line in grid:
        new_grid.append(line.copy())
    return new_grid


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

