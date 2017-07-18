# Advent of Code 2016: Day 8, Part 2
# Gregor Ulm



def rect(m, x, y):
    for col in range(x):
        for row in range(y):
            m[row][col] = 1
    return m


def rotateRow(m, row, c):

    # extract row, replace by shift version

    old_row = m[row]
    new_row = rotate(old_row, c)
    m[row]  = new_row

    return m


def rotateCol(m, col, c):

    acc = []

    # extract column
    for i in range(len(m)):
        acc.append(m[i][col])

    # rotate
    acc = rotate(acc, c)

    # insert rotated column
    for i in range(len(m)):
        m[i][col] = acc[i]

    return m


def rotate(lst, n):
    pos = len(lst) - n
    return lst[pos:] + lst[:pos]


def main():

    f     = open("input")
    data  = f.readlines()

    m      = []
    WIDTH  = 50
    HEIGHT = 6


    for i in range(HEIGHT):
        m.append([0] * WIDTH)


    for line in data:

        if line.startswith("rect"):

            # extract values
            tmp = line.split()[1]
            (x, y) = tmp.split("x")
            x = int(x)
            y = int(y)

            m = rect(m, x, y)


        elif line.startswith("rotate"):

            tmp    = line.split("=")[1]
            tmp    = tmp.split("by")
            (x, y) = tmp[0], tmp[1]

            x = int(x)
            y = int(y)

            if line.startswith("rotate row"):
                m = rotateRow(m, x, y)

            elif line.startswith("rotate column"):
                m = rotateCol(m, x, y)


    for row in m:
        s = ""
        for c in row:
            if c == 1:
                s += "#"
            elif c == 0:
                s += " "
        print(s)



main()
