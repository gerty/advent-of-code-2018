# Code written by @gerty

# Input from Day 25 Advent of Code 2018
# Input files in same directory
# My input: in file Day 25 puzzle input.txt

with open('Day 25 puzzle input.txt', 'r') as f:
    filedata = f.readlines()

allstars = []

for line in filedata:   # parse out the input, formatted with 4-D points separated by commas
    parsed = line.split(',')
    allstars.append([int(parsed[0]),
                      int(parsed[1]),
                      int(parsed[2]),
                      int(parsed[3])])

# So far I'm thinking that if I run through the large collection of stars, finding stars
# that are within 3 "blocks" of each other, I can then eliminate them one by one from the larger
# collection, until there are no more stars in the original set.

# I will need to start with one star in the collection, and find the Manhattan distance to the
# rest of the stars. Any star within 3 will become the next star in that constellation, and be removed
# from the larger collection. If no close stars are found then there is only one star in that constellation.

# I need two levels of removal. First, removing the star from the larger set once it has been identified,
# but then parsing out constellations as they form. As new stars are found in each constellation, they need
# to be counted, and emptied from the original collection. Only the current constellation needs to be maintained.


def get_manhattan_distance(point1,point2):  # a function to determine the Manhattan distance between two points
    distance = 0
    if len(point1) == len(point2):  # protect for points having different lengths
        for i in range(len(point1)):  # this function finds M-distance for points of any dimension
            distance += abs(point1[i]-point2[i])
    return distance

print(allstars)  # this is my collection of stars before searching
constellation_collection = []  # this is a list of constellations(list of stars(list of 4D points(int)))
constellation = []  # this will hold each constellation while we're working on it

print('There are {} stars to start.'.format(len(allstars)))

while allstars:  # then repeat this process until allstars is empty
    if not constellation:  # if our constellation of interest is empty
        this_star = allstars[0]  # grab a star from the list
        const_index = 0  # we begin to load up our constellation with the first star
        constellation.append(this_star.copy())  # and we load a copy of our first star in a new constellation
        allstars.remove(this_star)  # remove it from the collection of stars
        print('Removed star, put in constellation, now: {}.'.format(constellation))
        # at this point we're at the beginning of a new constellation

    for basestar in allstars:  # cycle through all of the stars to find others in this constellation
        # print('Comparing {} to {} for M-distance.'.format(basestar, constellation[const_index]))
        if get_manhattan_distance(basestar, constellation[const_index]) <= 3:
            constellation.append(basestar.copy())  # tack a copy at end of the constellation
            print('Added {} to our constellation! Now: {})'.format(basestar, constellation))

    for basestar in constellation:
        if basestar in allstars:
            allstars.remove(basestar)  # remove any stars from allstars that were put in the new constellation

    # Are we at the end of our current constellation? That would mean that there are no more stars to add.
    if const_index == len(constellation) - 1:  # if we didn't tack on any more stars
        print('Constellation complete: {}'.format(constellation))
        constellation_collection.append(constellation.copy())
        constellation.clear()
    else:
        const_index += 1
        print('More stars added. Now at index: {}.'.format(const_index, len(constellation)))

if constellation:
    print('Constellation complete: {}'.format(constellation))
    constellation_collection.append(constellation.copy())

print("Total number of constellations = {}".format(len(constellation_collection)))

# Returned 324 constellations
