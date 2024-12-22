#!/usr/bin/python3
import sys

data= []
with open(sys.argv[1], "r") as fp:
    data = fp.readlines()

for line in data:
    line = line[:-1]
    print(line[::-1])
