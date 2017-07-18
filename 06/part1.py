# Advent of Code 2016: Day 6, Part 1
# Gregor Ulm


def main():

    f     = open("input")
    data  = f.readlines()


    ch0 = dict()
    ch1 = dict()
    ch2 = dict()
    ch3 = dict()
    ch4 = dict()
    ch5 = dict()
    ch6 = dict()
    ch7 = dict()

    allDicts = [ch0, ch1, ch2, ch3, ch4, ch5, ch6, ch7]

    for line in data:
        line = line.strip()

        for i in range(len(line)):

            char = line[i]
            if char not in allDicts[i].keys():
                allDicts[i][char] = 1
            else:
                allDicts[i][char] += 1

    phrase = ""
    for d in allDicts:
        count  = 0
        letter = ""
        for char in d.keys():
            char_count = d[char]
            if char_count > count:
                count  = char_count
                letter = char

        phrase += letter

    print(phrase)


main()
