# Code written by @gerty

# Input from Day 5 of Advent of Code 2018
# Input files in same directory: Day 5 puzzle input.txt

polymer = []

with open('Day 5 puzzle input.txt', 'r') as f:  # open file for reading into polymer, char by char
    while True:
        c = f.read(1)
        if not c:  # EOF
            break
        polymer.append(c)

# Now collapse the entire text string to eliminate all opposite case neighbors.

result = [polymer[0]]  # Always start with the first element loaded into the result
print('result length = ')
print(len(result))
index = 1  # start evaluating at second location
while index < len(polymer):  # go until the end
    result.append(polymer[index])  # tack on the next character
    print('Result length =')
    print(len(result))
    if (len(result)>1):  # Protect for len=1,0 case
        r1 = result[-2]  # This should look at the second to last element
    else:
        r1 = ' '
    r2 = str.swapcase(result[-1])  # This should look at the opposite case of the last element
    if r1 == r2:  # compare the two
        print(result[-2:])
        result = result[:-2]  # shave off the end (WHY is there a "IndexError: list index out of range" here???)
    index += 1  # increment polymer to the next char of interest

print(len(result))

# Shower worked, but realistic answer 3508 is now too low.
# Next day, 11816 is too high, after I found an obvious bug. Let's see if I can find the not-so-obvious bugs.
# 11815 is too high
# 11744 is incorrect (tried ranging only to len(activepoly)-1)
# Looking at the problem again, I think my issue is that I'm making multiple passes, instead of one thorough one.
# Result 9348 is correct (needed to protect for the len = 1 case)
