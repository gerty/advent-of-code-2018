# Code written by @gerty

# Input from Day 5 of Advent of Code 2018
# Input files in same directory: Day 5 puzzle input.txt

polymer = []

with open('Day 5 puzzle input.txt', 'r') as f:
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break
        print("Read a character:", c)
        polymer.append(c)

answer = 0  # This will be the answer
print(polymer)

def collapse(poly):
    nextPoly = poly[0]  # Always start with the first element loaded
    done = False
    while not done:
        done = True
        for p in range(1,len(poly)):  # start at one more than beginning
            if poly[p] == str.swapcase(poly[p-1]):  # compare with previous character
                nextPoly = nextPoly[:-1]  # shave off the end by one
                done = False  # you did some change to the string, so you're not done
            else:
                nextPoly += poly[p]  # in this case, just tack on the character
        print(len(nextPoly))
    return nextPoly

collapse(polymer)
print(polymer)
answer = len(polymer)
print(answer)

# Saw length of nextPoly getting greater each time through. No bueno. Will think about this in the shower.