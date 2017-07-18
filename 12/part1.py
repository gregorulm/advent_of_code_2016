# Advent of Code 2016: Day 12, Part 1
# Gregor Ulm



def main():

    f            = open("input")
    instructions = f.readlines()

    reg = { "a" : 0 ,
            "b" : 0 ,
            "c" : 0 ,
            "d" : 0 }

    pos = 0
    while pos < len(instructions):

        x = instructions[pos]

        if x.startswith("inc"):
            r       = x.split()[1]
            reg[r] += 1


        elif x.startswith("dec"):
            r       = x.split()[1]
            reg[r] -= 1


        elif x.startswith("cpy"):

            tmp = x.split()
            val = tmp[1]
            r   = tmp[2]

            if val in reg.keys():
                reg[r] = reg[val]

            else:
                reg[r] = int(val)


        elif x.startswith("jnz"):

            tmp      = x.split()
            sentinel = tmp[1]

            if sentinel in reg.keys():
                if reg[sentinel] != 0:
                    pos += int(tmp[2])
                    continue

            else:
                if int(sentinel) != 0:
                    pos += int(tmp[2])
                    continue


        pos += 1


    print(reg["a"])



main()

