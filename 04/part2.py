# Advent of Code 2016: Day 4, Part 2
# Gregor Ulm



def shiftLine(raw, shift):

    result = ""

    for c in raw:

        if c == " ":
            result += c
            continue

        result += chr(97 + ((ord(c) - 97 + shift) % 26))

    return result


def main():

    f     = open("input")
    data  = f.readlines()


    for line in data:

        raw = line.split("-")

        tag = raw[-1]
        raw = raw[:-1]

        (id_val, checksum) = tag.split("[")
        id_val             = int(id_val)
        checksum           = checksum[:-2]


        letters = dict()
        for block in raw:
            for c in block:
                if c not in letters.keys():
                    letters[c] = 1
                else:
                    letters[c] +=1

        sums = []
        for k in letters.keys():
            sums.append((k, letters[k]))

        # TimSort preserves the order of elements, thus it is possible
        # to simply sort twice, first by letter, then by count, in order
        # to achieve the desired results
        sums = sorted(sums, key = lambda x : x[0])
        sums = sorted(sums, key = lambda x : x[1], reverse=True)

        letters = ""
        for (letter, _) in sums:
            letters += letter


        if letters.startswith(checksum):
            # replace dash with space; shift afterwards
            shift = id_val % 26 # saving CPU cycles
            raw   = " ".join(raw)

            tmp = shiftLine(raw, shift)
            if "north" in tmp: #North Pole objects"
                print(tmp, id_val)


main()
