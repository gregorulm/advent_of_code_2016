# Advent of Code 2016: Day 3, Part 1
# Gregor Ulm



def main():

    f     = open("input")
    data  = f.readlines()
    count = 0

    for line in data:

        (a, b, c) = tuple(line.split())

        a = int(a)
        b = int(b)
        c = int(c)

        if a + b > c and a + c > b and b + c > a:
            count += 1

    print(count)



main()
