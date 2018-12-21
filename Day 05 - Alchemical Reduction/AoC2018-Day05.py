# Code written by @gerty

# Input from Day 5 of Advent of Code 2018
# Input files in same directory: Day 5 puzzle input.txt

original = []

with open('Day 5 puzzle input.txt', 'r') as f:  # open file for reading into polymer, char by char
    while True:
        c = f.read(1)
        if not c:  # EOF
            break
        original.append(c)


# Now collapse the entire text string to eliminate all opposite case neighbors.

def collapsed_size(polymer):
    result = [polymer[0]]  # Always start with the first element loaded into the result
    index = 1  # start evaluating at second location
    while index < len(polymer):  # go until the end
        result.append(polymer[index])  # tack on the next character
        if len(result) > 1:  # Protect for len=1,0 case
            r1 = result[-2]  # This should look at the second to last element
        else:
            r1 = ' '
        r2 = str.swapcase(result[-1])  # This should look at the opposite case of the last element
        if r1 == r2:  # compare the two
            result = result[:-2]  # shave off the end (WHY is there a "IndexError: list index out of range" here???)
        index += 1  # increment polymer to the next char of interest
    return(len(result))

print(collapsed_size(original))

# Now on to part 2
sample = []
for letter in range(ord('a'), ord('z')+1):
    sample[:] = [x for x in original if ((x != chr(letter)) and (x != str.swapcase(chr(letter))))]
    print(chr(letter) + ' = ' + str(collapsed_size(sample)))
    sample.clear()

# This approach was much easier. Remember to def earlier next time.