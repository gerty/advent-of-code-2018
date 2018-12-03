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
# 4600 is too low, 4940 is correct!

def OneCharDiffers(a, b):
    result = -1;
    pos = 0;
    for letter in a:
        if letter != b[pos]:
            if result == -1:  # if diff was not seen yet
                result = pos
            else:
                return -1  # different char was seen before, exit with error
        pos += 1
    return result  # exit with answer or error, depending on whether diff was seen exactly once or not

for line in filedata:
    for compline in filedata:
        uncommon = OneCharDiffers(line, compline)  # find out position of character that differs, -1 if none/many
        if uncommon > 0:
            print(line[:uncommon]+line[uncommon+1:])

# Winning string is 'wrziyfdmlumeqvaatbiosngkc' with my input