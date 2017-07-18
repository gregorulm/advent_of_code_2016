# Advent of Code 2016: Day 4, Part 1
# Gregor Ulm



def main():

    f     = open("input")
    data  = f.readlines()
    total = 0


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
            total += id_val

    print(total)



main()
