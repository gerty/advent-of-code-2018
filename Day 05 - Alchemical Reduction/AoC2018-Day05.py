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

answer = 0  # This will be the answer
print(polymer)  # check for realistic input


def collapse(poly):  # This function will collapse the entire text string to eliminate all opposite case neighbors
    activepoly = poly  # this loads the polymer string for the first time
    done = False
    while not done:
        nextpoly = []  # this is our new iteration (but possibly not the last before we leave)
        nextpoly += poly[0]  # Always start with the first element loaded
        done = True
        for p in range(1, len(activepoly)):  # start at one more than beginning, go until the end
            if activepoly[p] == str.swapcase(activepoly[p-1]):  # compare with previous character
                nextpoly = nextpoly[:-1]  # shave off the end by one
                done = False  # you did some change to the string, so you're not done
            else:
                nextpoly += activepoly[p]  # in this case, just tack on the character
        print(len(nextpoly))
        activepoly = nextpoly
    return activepoly

polymer = collapse(polymer)
print(polymer)
answer = len(polymer)
print(answer)

# Saw length of nextPoly getting greater each time through. No bueno. Will think about this in the shower.
# Shower worked, but realistic answer 3508 is now too low.
# Next day, 11816 is too high, after I found an obvious bug. Let's see if I can find the not-so-obvious bugs.
