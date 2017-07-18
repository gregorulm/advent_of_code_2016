# Advent of Code 2016: Day 1, Part 1
# Gregor Ulm


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





def main():

    f = open("input")

    #line = "R2, L3"
    #line = "R2, R2, R2"
    #line = "R5, L5, R5, R3"

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

        if direction == "North":
            y += steps

        elif direction == "East":
            x += steps

        elif direction == "South":
            y -= steps

        elif direction == "West":
            x -= steps


    print( abs(x) + abs(y) )


main()
