

# Code written by @gerty

# Input from Day 8, Problem 1 (and 2) of Advent of Code 2016
# Input files in same directory
# My input: in file D8input.txt

with open('Day01-INPUT.txt', 'r') as f:
    filedata = f.readlines()

tally = 0
tallies = []
found = False;

for line in filedata:
    data = line.split()
    tally += int(data[0])
print(tally)

tally = 0
while found == 0:
    for line in filedata:
        data = line.split()
        tally += int(data[0])
        if tally in tallies:
            print('Found this one twice: ')
            print(tally)
            found = True;
        tallies.append(tally)

# Ran slowly because of course there are optimization to be had that I didn't do.
# Also, how do I combine strings and ints again...? welcome back to the learning curve.