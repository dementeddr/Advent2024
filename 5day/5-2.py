#!/usr/bin/python3

import sys
import re
import math
import functools
from time import perf_counter_ns
from collections import defaultdict

_day = 5 #Advent of Code day

## BEGIN SOLUTION

befores = defaultdict(list)
afters = defaultdict(list)


def main(data):

    doing_updates = False
    score = 0

    for line in data:

        if line == '\n':
            doing_updates = True
            continue
        
        if not doing_updates:
            pages = list(map(int, line.split('|')))

            befores[pages[1]].append(pages[0])
            afters[pages[0]].append(pages[1])
        
        else:
            update = list(map(int, line.split(",")))
            
            if check_update(update):
                continue

            print(f"WRONG: {update}")
            fixed = sorted(update, key=functools.cmp_to_key(comp_pages))
            print(f"FIXED: {fixed}")
            mid = fixed[math.floor(len(fixed)/2)]
            score += mid
            print(f"SCORE: +{mid} = {score}")
            print()

    print(f"SCORE = {score}")


def comp_pages(page1, page2):
    if page1 in afters[page2]:
        return 1
    if page2 in afters[page1]:
        return -1
    return 0


def check_update(update):
    #print(f"Check {update}")
    for i, page in enumerate(update):
        #print(f"  [{i}]: {page}")
        #print(f"  befores: {befores[page]}")
        #print(f"  afters: {afters[page]}")
        #print("    ", end="")
        for b in update[:i]:
            #print(f"{b}, ", end="")
            if b in afters[page]:
                return False
        #print(end="\n    ")
        for a in update[i+1:]:
            #print(f"{a}, ", end="")
            if a in befores[page]:
                return False
        #print()

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

