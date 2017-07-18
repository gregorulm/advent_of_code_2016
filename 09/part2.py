# Advent of Code 2016: Day 9, Part 2
# Gregor Ulm



def decompress(x, y, s):

    front = s[:x]

    return (front * y, s[x:])



def main():

    f    = open("input")
    data = f.readlines()
    data = "".join(data)
    data = data.strip()

    total = 0 # this is a 'long' integer by default in Python 3


    i = 0
    while True:

        if i % 250000 == 0:
            print(total, len(data))

        try:
            pos = data.index("(")

        except ValueError:
            #acc += data
            total += len(data)
            break


        end    = data.index(")", pos)
        total += len(data[:pos])

        marker = data[pos + 1 : end]
        (x, y) = marker.split("x")
        x = int(x)
        y = int(y)

        (front, data) = decompress(x, y, data[end + 1:])
        data = front + data

        i += 1

    print(total)



main()

