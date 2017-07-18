# Advent of Code 2016: Day 7, Part 1
# Gregor Ulm


def hasAnnotation(s):

    if len(s) <= 3:
        return False

    else:
        top = s[0:4]
        if top[0] == top[3] and top[1] == top[2] and top[0] != top[1]:
            return True

        else:
            return hasAnnotation(s[1:])



def splitWith(char, s):

    if char in s:
        pos   = s.index(char)
        return (s[:pos], s[pos + 1:])

    return(s, "")



def extractParts(line):
    outside = []
    inside  = []

    isOutside = True

    while not line == "":

        if isOutside:
            (front, line) = splitWith("[", line)
            outside.append(front)
            isOutside = False

        else:
            (front, line) = splitWith("]", line)
            inside.append(front)
            isOutside = True

    return (outside, inside)


def main():

    f     = open("input")
    data  = f.readlines()

    count = 0

    for line in data:

        (outside, inside) = extractParts(line)

        outsideOK = False
        insideOK  = True

        for elem in outside:
            if hasAnnotation(elem):
                outsideOK = True

        for elem in inside:
            if hasAnnotation(elem):
                insideOK = False

        if outsideOK and insideOK:
            count += 1

    print(count)


main()
