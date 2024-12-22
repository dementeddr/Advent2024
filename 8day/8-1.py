#!/usr/bin/python3

import sys
import re
from collections import defaultdict
from time import perf_counter_ns

_day = 8 #Advent of Code day

## BEGIN SOLUTION

height = 0
width = 0

def main(data):

    antennae = defaultdict(list)
    anodes = set()
    global width
    global height
    width = len(data[0])-1
    height = len(data)

    print(f"width={width}, height={height}")

    for y, line in enumerate(data):
        for x, spot in enumerate(line[:-1]):
            if spot != '.':
                antennae[spot].append((x, y))
                
    for freq in sorted(antennae):
        print(f"{freq}: {antennae[freq]}")
        anodes.update(find_freq_antinodes(antennae[freq]))

    print_nodes(data, anodes)
    print(f"Antinode count: {len(anodes)}")


def find_freq_antinodes(ants):
    
    anodes = set()

    for i, s1 in enumerate(ants[:-1]):
        for s2 in ants[i+1:]:
            anodes.update(find_stat_antinodes(s1, s2))
    
    return anodes


def find_stat_antinodes(s1, s2):
    
    anodes = set()

    dx = s1[0] - s2[0]
    dy = s1[1] - s2[1]
    print(f"{s1}--{s2} = d({dx}, {dy})")
   
    onode1 = (s1[0] + dx, s1[1] + dy)
    print(f"  {onode1}")
    if is_in_range(onode1):
        anodes.add(onode1)

    onode2 = (s2[0] - dx, s2[1] - dy)
    print(f"  {onode2}")
    if is_in_range(onode2):
        anodes.add(onode2)

    #keep for part 2
    #if (s1[0] - s2[0]) % 3 == 0 and (s1[1] - s2[1]) % 3 == 0:
    return anodes


def is_in_range(coord):
    if coord[0] < 0 or coord[0] >= width:
        return False
    if coord[1] < 0 or coord[1] >= height:
        return False
    return True


def print_nodes(data, anodes):
    print()
    for y, line in enumerate(data):
        out = []
        for x, spot in enumerate(line[:-1]):
            if (x,y) in anodes:
                out.append('#')
            else:
                out.append(spot)
        print(''.join(out))


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

