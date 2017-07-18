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



def outside(s, outsideSpotted):

    (front, back) = splitWith("[", s)

    if front == "":
        return outsideSpotted

    if outsideSpotted:
        return inside(back, True)

    else:
        if hasAnnotation(front):
            return inside(back, True)
        else:
            return inside(back, False)



def inside(s, outsideSpotted):

    (front, back) = splitWith("]", s)

    if s == "":
        return outsideSpotted

    if hasAnnotation(front):
        return False
    else:
        return outside(back, outsideSpotted)



def splitWith(char, s):

    if char in s:
        pos   = s.index(char)
        return (s[:pos], s[pos + 1:])

    return(s, "")



def main():


    f     = open("input")
    data  = f.readlines()
    count = 0

    for line in data:
        if outside(line, False): # entry point to mutual recursion
            count += 1

    print(count)

main()
