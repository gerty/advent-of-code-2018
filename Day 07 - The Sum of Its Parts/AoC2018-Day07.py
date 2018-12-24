# Code written by @gerty

# Input from Day 7 Advent of Code 2018
# Input files in same directory
# My input: in file Day 7 puzzle input.txt

with open('Day 7 puzzle test input.txt', 'r') as f:
    filedata = f.readlines()

allrules = []  # contains all the rules in [complete this step first, before this step] format
steps = {}  # tallies all steps and keeps track of how many prereqs there are

for line in filedata:   # parse out the input
    parsed = line.split()
    allrules.append(parsed[1] + parsed[7])  # organize the rules in a two-character array

for rule in allrules:  # cycle through each rule
    if rule[1] not in steps:
        steps[rule[1]] = 1  # create a new index if it doesn't exist
    else:
        steps[rule[1]] += 1  # increment each letter's index by one

answer = ''

while steps:  # if there are still steps to be done

    for step in sorted(steps):  # cycle through prereq count dictionary, in alpha order
        if steps[step] == 0:  # if there are no more barriers to performing the step
            answer += letter  # our answer became better

            for rule in allrules:
                if letter == rule[0]:  # "step 1 must be completed before step 2 can start"
                    steps[rule[1]] -= 1;  # reduce the number of prereqs by one
            print(allrules)

            del steps[letter]  # but we need to delete the step so we don't do it again

print(answer)


# So close....