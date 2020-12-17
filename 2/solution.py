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


#data=["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]

# Solution 1
fails=0

# Data parsing
db=[]
for line in data:
    policy_raw, match, password = line.split(" ")
    match = match.rstrip(":")
    policy = {}
    policy["low"], policy["high"] = policy_raw.split("-")
    policy["low"] = int(policy["low"])
    policy["high"] = int(policy["high"])
    db.append({"policy":policy,"match":match,"password":password,"count":password.count(match)})
    
pprint(db)
for entry in db:
    if entry["count"] < entry["policy"]["low"] or entry["count"] > entry["policy"]["high"]:
        fails += 1

print("Total valid: " + str(len(data)-fails))

# Solution 2
fails=0

# Allow index 0 matching
for entry in db:
    entry["policy"]["low"] -= 1
    entry["policy"]["high"] -=1

for entry in db:
    entry["count"] = 1 if entry["password"][entry["policy"]["low"]:(entry["policy"]["low"]+1)] == entry["match"] else 0
    entry["count"] += 1 if entry["password"][entry["policy"]["high"]:(entry["policy"]["high"]+1)] == entry["match"] else 0
    if entry["count"] != 1:
        pprint(entry)
        fails += 1

print("Total valid: " + str(len(data)-fails))
