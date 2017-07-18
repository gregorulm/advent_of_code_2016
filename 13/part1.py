# Advent of Code 2016: Day 13, Part 1
# Gregor Ulm


# k: (x, y), v: shortest number of steps or '#' if wall
MAZE = dict()
NUM  = None # puzzle input


def getNeighbors(pos: (int, int)):

    (x, y)    = pos
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    res       = []
    for (x, y) in neighbors:
        # limit size of area:
        if x >= 0 and y >= 0 and x <= 50 and y <= 50:
            if (x, y) not in MAZE.keys():
                res.append((x, y))

    return res



def lookupNeighbors(pos):

    (x, y) = pos
    ns     = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    res    = []
    for x in ns:
        if x in MAZE.keys() and MAZE[x] != "#":
            res.append(x)

    return res



def tileVal(pos: (int, int)):

    (x, y) = pos
    num    = x * x + 3 * x + 2 * x * y + y + y * y
    num   += NUM

    # convert to binary
    num = "{0:b}".format(num)

    """
    cf. problem statement:

    Find the binary representation of that sum; count the number of bits
    that are 1.
    If the number of bits that are 1 is even, it's an open space.
    If the number of bits that are 1 is odd, it's a wall.
    """

    ones = 0
    for c in num:
        if c == "1":
            ones += 1

    if ones % 2 == 0:
        return "."        # open space

    return "#"            # wall



def done(pos):

    (x, y)    = pos
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for n in neighbors:
        if n not in MAZE.keys():
            return False

    return True





def main():
    global NUM, MAZE

    # puzzle input
    NUM         = 1362
    goal        = (31, 39)

    start       = (1,1)
    MAZE[start] = 0
    frontier    = [start]

    while not frontier == []:

        # by sorting, the correct solution can be found, but this is due
        # to the nature of the solution; the code below properly solves
        # this problem, so that it would presumably work with any input

        #frontier = sorted(frontier, reverse = True)

        tile      = frontier.pop()
        steps     = MAZE[tile]
        neighbors = getNeighbors(tile)

        tiles     = MAZE.keys()

        for n in neighbors:

            if n not in tiles:

                val = tileVal(n)

                if val != "#":
                    MAZE[n] = steps + 1
                    frontier.append(n)

                else:
                    MAZE[n] = "#"



    """
    After exploring the maze we may need to update the minimum steps
    for each tile. We will do this iteratively until no further change
    can be made. This may not be the most elegant way, but the code is
    rather straightforward.
    """


    while True:

        changes = 0
        ks      = MAZE.keys()

        for k in ks:

            if MAZE[k] == "#":
                continue

            else:
                val = MAZE[k]
                ns  = lookupNeighbors(k)

                for n in ns:

                    if MAZE[n] != "#":
                        if MAZE[n] > (val + 1):

                            MAZE[n] = val + 1
                            changes += 1

        if changes == 0:
            break


    print(MAZE[goal])



main()


