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
    occurancecount = 0
    for c in data[0]:
        if data[0].count(c) > occurancecount:
            occurancecount = data[0].count(c)
    if occurancecount >= 3:
        threetimes += 1
    elif occurancecount >=2:
        twotimes += 1
print('twotimes')
print(twotimes)
print('threetimes')
print(threetimes)
print('CHECKSUM')
print(twotimes*threetimes)
# 4600 is too low