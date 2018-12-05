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

print(polymer)  # check for realistic input

def collapse(poly):  # This function will collapse the entire text string to eliminate all opposite case neighbors
    activepoly = poly  # this loads the polymer string for the first time
    done = False
    while not done:
        nextpoly = [activepoly[0]]  # Always start with the first element loaded
        done = True
        for p in range(1, len(activepoly)):  # start at one more than beginning, go until the end
            if activepoly[p] == str.swapcase(activepoly[p-1]):  # compare with previous character
                print(activepoly[p-1] + activepoly[p])
                nextpoly = nextpoly[:-1]  # shave off the end by one if we find a match, and don't add to it
                done = False  # you did some change to the string, so you're not done
            else:
                nextpoly.append(activepoly[p])  # in this case, just tack on the character
        print(len(nextpoly))
        activepoly = nextpoly
    return activepoly

print(len(collapse(polymer)))

# Saw length of nextPoly getting greater each time through. No bueno. Will think about this in the shower.
# Shower worked, but realistic answer 3508 is now too low.
# Next day, 11816 is too high, after I found an obvious bug. Let's see if I can find the not-so-obvious bugs.
