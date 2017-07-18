# Advent of Code 2016: Day 5, Part 2
# Gregor Ulm


import hashlib

def main():

    password = [None, None, None, None, None, None, None, None]

    s = "ugkcyxxp"

    i = 0

    while True:
        tmp = s + str(i)
        val = hashlib.md5(tmp.encode('utf-8')).hexdigest()

        if val.startswith("00000"):

            """
            The sixth character represents the position (0-7), and the seventh character is the character to put in that position.
            """

            pos = val[5]

            if pos in "01234567":
                pos = int(pos)

                if password[pos] == None:
                    print(val)
                    password[pos] = val[6]


        if None not in password:
            break

        i += 1


    password = ''.join(password)
    print(password)

main()
