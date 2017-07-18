# Advent of Code 2016: Day 2, Part 1
# Gregor Ulm


def main():

    # data = "ULL\nRRDDD\nLURDL\nUUUUD".split()

    f    = open("input")
    data = f.readlines()

    pos  = (1, 1)
    code = ""

    (row, col) = pos

    for line in data:

        for move in line:

            if   move == "U":
                if row == 0:
                    continue
                else:
                    row -= 1

            elif move == "D":
                if row == 2:
                    continue
                else:
                    row += 1

            elif move == "L":
                if col == 0:
                    continue
                else:
                    col -= 1

            elif move == "R":
                if col == 2:
                    continue
                else:
                    col += 1

        num   = 3 * row + col + 1 # convert coordiate to number
        code += str(num)

    print(code)


main()
