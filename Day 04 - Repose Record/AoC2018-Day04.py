# Code written by @gerty

# Input from Day 4, Problem 1 of Advent of Code 2018
# Input files in same directory
# My input: in file Day 4 puzzle input.txt

import re

with open('Day 4 puzzle input.txt', 'r') as f:
    filedata = f.readlines()

answer = 0  # This will be the answer
filedata.sort()  # first we have to sort the data - timestamps are a quick way to do this with raw data

guardNum = 0  # initialize a few vars to put the data in
fallsMin = 0
wakesMin = 0

guardRecord = []  # one record of a guard's sleeping activities
guardsTable = []  # entire array of multiple activities
sleepRecord = {}  # lookup table of the combined sleeping record of each guard
for line in filedata:
    parsed = line.split()
    print(parsed)
    if len(parsed) == 6:  # line is marking a guard beginning his shift
        guardNum = int(parsed[3][1:])
    elif parsed[2] == 'falls':
        fallsMin = int(parsed[1][3:5])
    elif parsed[2] == 'wakes':
        wakesMin = int(parsed[1][3:5])

        guardRecord = [guardNum, fallsMin, wakesMin, wakesMin-fallsMin]
        guardsTable.append(guardRecord)

emptyRecord = [0 for item in range(60)]

hour = emptyRecord
for record in guardsTable:
    if record[0] not in sleepRecord:
        sleepRecord[record[0]] = emptyRecord
    hour = sleepRecord[record[0]]

    for thisMinute in range(record[1], record[2]):
        hour[thisMinute] += 1
    sleepRecord[record[0]] = hour

print(guardsTable)
print(sleepRecord)