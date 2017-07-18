# Advent of Code 2016: Day 3, Part 2
# Gregor Ulm



def main():

    f     = open("input")
    data  = f.readlines()
    count = 0


    col_1 = []
    col_2 = []
    col_3 = []

    for line in data:

        (a, b, c) = tuple(line.split())

        a = col_1.append(int(a))
        b = col_2.append(int(b))
        c = col_3.append(int(c))


    for elem in [col_1, col_2, col_3]:

        while True:
            a = elem[0]
            b = elem[1]
            c = elem[2]
            if a + b > c and a + c > b and b + c > a:
                count += 1

            elem = elem[3:]
            if elem == []:
                break


    print(count)


main()
