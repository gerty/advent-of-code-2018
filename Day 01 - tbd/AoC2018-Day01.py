

# Code written by @gerty

# Input from Day 8, Problem 1 (and 2) of Advent of Code 2016
# Input files in same directory
# My input: in file D8input.txt

with open('Day01-INPUT.txt', 'r') as f:
    filedata = f.readlines()

tally = 0
tallies = []


for line in filedata:
    data = line.split()
    tally += int(data[0])
print(tally)

tally = 0

for line in filedata:
    data = line.split()
    tally += int(data[0])
    if tally in tallies:
        print('Found this one twice: ' + tally)
    tallies.append(tally)
    print(tally)

# Here it goes...