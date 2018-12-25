# Code written by @gerty

# Input from Day 7 Advent of Code 2018
# Input files in same directory
# My input: in file Day 7 puzzle input.txt

with open('Day 7 puzzle input.txt', 'r') as f:
    filedata = f.readlines()

allrules = []  # contains all the rules in [complete this step first, before this step] format
steps = {}  # tallies all steps and keeps track of how many prereqs there are

for line in filedata:   # parse out the input
    parsed = line.split()
    allrules.append(parsed[1] + parsed[7])  # organize the rules in a two-character array

for rule in allrules:  # cycle through each rule
    if rule[0] not in steps:
        steps[rule[0]] = 0  # create a new index if it doesn't exist
    if rule[1] not in steps:
        steps[rule[1]] = 0  # create a new index if it doesn't exist
    steps[rule[1]] += 1  # increment a step's index by one if it has a prereq

answer = ''

while steps:  # if there are still steps to be done
    print(sorted(steps))

    for step in sorted(steps):  # cycle through prereq count dictionary, in alpha order
        if steps[step] == 0:  # if there are no more barriers to performing the step
            answer += step  # our answer became better by adding the step

            for rule in allrules:
                if step == rule[0]:  # "step 1 must be completed before step 2 can start"
                    steps[rule[1]] -= 1  # reduce the number of prereqs by one

            del steps[step]  # but we need to delete the step so we don't do it again
            break  # break out of the loop because need to resort
        print(allrules)
        print(steps)


print(answer)


# It works. Need to link the list and the dictionary somehow to make it more Pythonic, but it works.