#!/usr/bin/python3

import argparse
import sys
from pprint import pprint


parser = argparse.ArgumentParser(description='Advent of Code: Day 1 Problem 1')
parser.add_argument('--input','-i', action="store",  help='Input file path')
args = parser.parse_args()

if args.input is None:
    print("Please provide an input file")
    sys.exit()

# Parse input file into data array to work with
# NOTE: Does not check if file exists first
data = []
with open(args.input, 'r') as f:
    for line in f:
        data.append(line.rstrip())

# Solution 1
for x in data:
    for y in data:
        if int(x) + int(y) == 2020:
            print(str(x) + " + " + str(y) + " = 2020")
            print(str(x) + " * " + str(y) + " = " + str(int(x)*int(y)))
            break

# Solution 2
# NOTE: This feels gross to me, there may be a better way without deep nesting
for x in data:
    for y in data:
        for z in data:
            if int(x) + int(y) + int(z) == 2020:
                print(x + " + " + y + " + " + z + " = 2020")
                print(x + " * " + y + " * " + z + " = " + str(int(x)*int(y)*int(z)))
                break
