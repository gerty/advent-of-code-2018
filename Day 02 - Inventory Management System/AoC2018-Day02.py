# Code written by @gerty

# Input from Day 8, Problem 1 (and 2) of Advent of Code 2016
# Input files in same directory
# My input: in file D8input.txt

with open('Day 2 puzzle input.txt', 'r') as f:
    filedata = f.readlines()

# and then separately counting those with exactly three of any letter.
# You can multiply those two counts together to get a rudimentary checksum

twotimes = 0
threetimes = 0
checksum = 0

for line in filedata:
    data = line.split()
    twocount = False
    threecount = False
    for c in data[0]:
        if data[0].count(c) == 2:
            twocount = True
        if data[0].count(c) == 3:
            threecount = True
    if twocount:
        twotimes += 1
    if threecount:
        threetimes += 1

checksum = threetimes * twotimes

print('twotimes')
print(twotimes)
print('threetimes')
print(threetimes)
print('CHECKSUM')
print(checksum)
# 4600 is too low