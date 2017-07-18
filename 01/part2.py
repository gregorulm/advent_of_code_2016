# Advent of Code 2016: Day 1, Part 2
# Gregor Ulm


positions = set()


def nextStep(direction, letter):

    order = ["North", "East", "South", "West"]
    pos    = order.index(direction)

    if letter == "R":
        pos += 1

    elif letter == "L":
        pos -= 1

    if pos == -1:
        pos = 3

    if pos == 4:
        pos = 0

    return order[pos]


def updatePositions(pos_from, steps, direction):

    (start_x, start_y) = pos_from
    vals               = []

    if direction == "North":
        for el in range(start_y + 1, start_y + steps + 1):
            val = (start_x, el)
            vals.append(val)

    elif direction == "East":
        for el in range(start_x + 1, start_x + steps + 1):
            val = (el, start_y)
            vals.append(val)

    elif direction == "South":
        for el in range(start_y - 1, start_y - steps - 1, -1):
            val = (start_x, el)
            vals.append(val)

    elif direction == "West":
        for el in range(start_x - 1, start_x - steps - 1, -1):
            val = (el, start_y)
            vals.append(val)


    for x in vals:
        if x in positions:
            (x, y) = x
            print( abs(x) + abs(y) )
            exit()
        else:
            positions.add(x)

    return (vals[-1])


def main():

    f = open("input")

    #line = "R8, R4, R4, R8"

    line = f.readline().strip()

    line += ","  # simplifies the loop below

    (x, y) = (0, 0)
    direction = "North"


    while True:

        pos = line.find(",")

        if pos == -1:
            break

        seg = line[:pos]
        seg = seg.strip()

        letter = seg[0]
        steps  = seg[1:].strip()
        steps  = int(steps)

        line = line[pos + 1:] # ignore comma

        direction = nextStep(direction, letter)
        pos_from  = (x, y)

        (x, y) = updatePositions(pos_from, steps, direction)


main()
