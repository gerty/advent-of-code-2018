# Code written by @gerty

# Input from Day 3, Problem 3 of Advent of Code 2018
# Input files in same directory
# My input: in file Day 3 puzzle input.txt

import re

with open('Day 3 puzzle input.txt', 'r') as f:
    filedata = f.readlines()

answer = 0
grid = [[0]*1000 for _ in range(1000)]

for line in filedata:
    parsed = re.findall(r'\d+',line)
    print(parsed)
    for x in range(int(parsed[1]),int(parsed[1])+int(parsed[3])):
        for y in range(int(parsed[2]),int(parsed[2])+int(parsed[4])):
            if grid[x][y] == 1:
                answer += 1
                grid[x][y] += 1
            else:
                grid[x][y] += 1
print(answer)
# 184130 is too high
# 153979 is too high
# 118322 is correct!