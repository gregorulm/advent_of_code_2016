# Advent of Code 2016: Day 9, Part 1
# Gregor Ulm



def decompress(x, y, s):

    front = s[:x]

    return (front * y, s[x:])


def main():

    f    = open("input")
    data = f.readlines()
    data = "".join(data)
    data = data.strip()

    acc  = ""

    while True:

        try:
            pos = data.index("(")

        except ValueError:
            acc += data
            break


        end    = data.index(")", pos)
        marker = data[pos + 1 : end]

        acc   += data[:pos]

        (x, y) = marker.split("x")
        x = int(x)
        y = int(y)

        (front, data) = decompress(x, y, data[end + 1:])
        acc += front


    print(len(acc))



main()
