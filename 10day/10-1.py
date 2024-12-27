#!/usr/bin/python3

import sys
import re
from collections import deque
from time import perf_counter_ns

_day = 10 #Advent of Code day

## BEGIN SOLUTION

dirs = [(0,-1), (1,0), (0,1), (-1,0)]
width = -1
height = -1

def main(data):

    global width
    global height

    trailmap = []
    heads = []
    score = 0
    step_graph = {}

    for line in data:
        trailmap.append(list(map(int, line.strip())))
    
    height = len(trailmap)
    width = len(trailmap[0])

    for y, line in enumerate(trailmap):
        for x, step in enumerate(line):
            step = trailmap[y][x]
            coord = (x, y)
            step_graph[coord] = find_nexts(coord, trailmap)
            if step == 0:
                heads.append(coord)

    for head in heads:
        score += score_head(head, step_graph, trailmap)

    print(f"Trailhead scores = {score}")


def score_head(head, step_graph, trailmap):
    
    stepq = deque()
    score = 0
    peaks = []

    for s in step_graph[head]:
        stepq.append(s)

    while len(stepq) > 0:
        step = stepq.popleft()
        if get_step(step, trailmap) == 9 and step not in peaks:
            score +=1
            peaks.append(step)
            continue
        for s in step_graph[step]:
            stepq.append(s)
    
    return score
        

def find_nexts(coord, trailmap):
    
    step = trailmap[coord[1]][coord[0]]
    children = []

    for di in dirs:
        ncoord = add_coord(coord, di)
        if not in_map(ncoord):
            continue
        astep = trailmap[ncoord[1]][ncoord[0]]
        if astep == step + 1:
            children.append(ncoord)
    
    return children


def get_step(coord, trailmap):
    return trailmap[coord[1]][coord[0]]


def add_coord(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])


def in_map(coord):
    return coord[0] >= 0 and coord[0] < width and coord[1] >= 0 and coord[1] < height


def print_map(trailmap):
    for line in trailmap:
        print(''.join(line))

    
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

