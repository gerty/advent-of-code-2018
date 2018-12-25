# Code written by @gerty

# Input from Day 25 Advent of Code 2018
# Input files in same directory
# My input: in file Day 25 puzzle input.txt

with open('Day 25 puzzle input.txt', 'r') as f:
    filedata = f.readlines()

allpoints = []

for line in filedata:   # parse out the input
    parsed = line.split(',')
    allrules.append([int(parsed[0]),
                     int(parsed[1]),
                     int(parsed[2]),
                     int(parsed[3])])
print(allrules)

