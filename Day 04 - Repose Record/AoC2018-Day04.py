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
for line in filedata:
    parsed = line.split()
    if len(parsed) == 6:  # line with 6 elements is marking a guard beginning his shift
        guardNum = int(parsed[3][1:])
    elif parsed[2] == 'falls':  # line with "falls" as third element is when guard falls asleep
        fallsMin = int(parsed[1][3:5])
    elif parsed[2] == 'wakes':  # line with "wakes" as third element is when guard wakes up
        wakesMin = int(parsed[1][3:5])  # only need to record an entry when an 'wake' event occurs
        guardRecord = [guardNum, fallsMin, wakesMin, wakesMin-fallsMin]
        guardsTable.append(guardRecord)

print(guardsTable)

sleepRecord = {}  # lookup table of the combined sleeping record of each guard

for record in guardsTable:
    if record[0] not in sleepRecord:
        sleepRecord[record[0]] = [0 for x in range(61)]  # init with zeros for every minute if guard is new

    hour = sleepRecord[record[0]]  # copy the existing sleep record of said guard (zeros if just created)

    for thisMinute in range(record[1], record[2]):  # loop through the awake hours (may need +1 here?)
        hour[thisMinute] += 1  # add an awake minute
    hour[60] += record[3]  # use the 61st slot to tally total sleep minutes
    sleepRecord[record[0]] = hour  # copy back to the master sleepRecord

print(sleepRecord)

for guard,hour in sleepRecord.items():  # cycle through records and add sleep time
    print(str(guard) + ' --- ' + str(hour[60]))
    print(hour)

#  Correct answer for part 1 was 72925

#  Most often asleep during a single minute was guard 1489 at the 33rd min, for 18 times.
#  Answer for part 2: 1489 * 33 = 49137
