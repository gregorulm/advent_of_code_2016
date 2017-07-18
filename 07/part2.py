# Advent of Code 2016: Day 7, Part 2
# Gregor Ulm


def findABA(s, acc):

    if len(s) <= 2:
        return acc

    else:
        top = s[0:3]
        if top[0] == top[2] and top[0] != top[1]:
            return findABA(s[1:], acc + [top])

        else:
            return findABA(s[1:], acc)


def makeBABs(abas):
    
    res = []
    
    for elem in abas:
        assert len(elem) == 3
        mid = elem[1]
        out = elem[0]
        
        res.append(mid + out + mid)

    return res


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



def containsBAB(bab, inside):
    
    for elem in inside:
        if bab in elem:
            return True
            
    return False
    
    

def main():

    f     = open("input")
    data  = f.readlines()
    count = 0

    for line in data:

        (outside, inside) = extractParts(line)
        allABA            = []
        
        for elem in outside:
            allABA += findABA(elem, [])
                            
        allBAB = makeBABs(allABA)
        
        for bab in allBAB:
            if containsBAB(bab, inside):
                count += 1
                break # avoids counting multiple ABA/BAB pairs

    print(count)

main()
