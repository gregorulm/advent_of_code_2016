# Advent of Code 2016: Day 14, Part 2
# Gregor Ulm

import hashlib

CACHE = dict()


def get_md5(s: str):

    return hashlib.md5(s.encode('utf-8')).hexdigest()



def get_md5_2016(s : str):

    start_s = s

    if start_s not in CACHE.keys():

        for i in range(0, 2016):
            s = get_md5(s)

        CACHE[start_s] = s

    return CACHE[start_s]



# find five-character sequence
def has_quintet(salt: str, start: int, quintet: str):

    for x in range(start, start + 1000):
        s = get_md5(salt + str(x))

        s = get_md5_2016(s)

        if quintet in s:
            return True

    return False



def first_triplet(s: str):

    for i in range(len(s)):
        if s[i:i+3] == s[i] * 3:
            return s[i] * 3

    return ""



def main():

    #salt   = "abc"
    salt   = "qzyelonm"
    index  = 0
    result = []



    while len(result) < 64:

        # process md5 hash
        sig = get_md5(salt + str(index))

        sig = get_md5_2016(sig)

        # find three-character sequence
        triplet = first_triplet(sig)


        if triplet != "":
            #print(index, sig)

            # find five-character sequence in next 1000 hashes
            quintet = triplet[0] * 5
            if has_quintet(salt, index + 1, quintet):
                result.append((index, sig))
                print(index, sig)

        index += 1


    print(result[63][0])



main()
