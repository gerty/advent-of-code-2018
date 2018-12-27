# Code written by @gerty

# Input from Day 25 Advent of Code 2018
# Input files in same directory
# My input: in file Day 25 puzzle input.txt

with open('Day 25 puzzle test input.txt', 'r') as f:
    filedata = f.readlines()

allstars = []

for line in filedata:   # parse out the input
    parsed = line.split(',')
    allstars.append([int(parsed[0]),
                      int(parsed[1]),
                      int(parsed[2]),
                      int(parsed[3])])

# So far I'm thinking that if I run through the large collection of stars, finding sets
# that are within 3 "blocks" of each other, I can then eliminate them one by one from the larger
# collection, until there are no more stars in the original set.

# I will need to start with one star in the collection, and find the Manhattan distance to the
# rest of the stars. Any star within 3 will become the next star in that constellation, and be removed
# from the collection. If no close stars are found then there is only one star in that constellation.

# I need two levels of removal. First, removing the star from the larger set once it has been identified,
# but then parsing out constellations as they form. As new stars are found in each constellation, they need
# to be put on the end of the constellation's queue, to search from there vantage point before declaring the
# constellation complete.

print(allstars)  # this is my collection of stars before searching
constellations = []  # this list of lists will be my constellations


def get_manhattan_distance(point1,point2):
    distance = 0
    for i in range(len(point1)):
        distance += abs(point1[i]-point2[i])
    return distance

starofinterest = allstars[0]  # arbitrarily start with one star
constofinterest = 0  # we begin to load up the first constellation
constellations[constofinterest].append(starofinterest.copy())  # and we load our first star in that constellation
starinconstellation = 0  # we start to look at the first star in that constellation
del allstars[0]  # remove it from the collection of stars
while allstars:
    for basestar in allstars:  # cycle through all of the stars to find others in this constellation
        if get_manhattan_distance(basestar,starofinterest) < 3:
            constellations[constofinterest].append(star.copy())  # tack a copy at end of the constellation
            del allstars[star]  # lookup and remove this star from consideration for other constellations
    if starofinterest == constellations[constofinterest][-1]:  # if we didn't tack on any more stars
        print('Constellation complete:')
        print(constellations[constofinterest])
        constofinterest += 1
        starinconstellation = 0
    else:
        starinconstellation += 1
        starofinterest = constellations[constofinterest][starinconstellation]
print(len(constellations))