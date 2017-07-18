# Advent of Code 2016: Day 5, Part 1
# Gregor Ulm


import hashlib

def main():

    password = ""
    s = "ugkcyxxp"

    i = 0

    count = 0
    while count < 8:
        tmp = s + str(i)
        val = hashlib.md5(tmp.encode('utf-8')).hexdigest()

        #print(val, type(val))

        if val.startswith("00000"):
            print(val)
            count += 1
            password += val[5]


        i += 1



    print(password)

main()

