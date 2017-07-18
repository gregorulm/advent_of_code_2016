# Advent of Code 2016: Day 14, Part 1
# Gregor Ulm

import hashlib



def get_md5(s: str):

    return hashlib.md5(s.encode('utf-8')).hexdigest()



# find five-character sequence
def has_quintuplet(salt: str, start: int, quintuplet: str):

    for x in range(start, start + 1000):
        s = get_md5(salt + str(x))

        if quintuplet in s:
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

        # find three-character sequence
        triplet = first_triplet(sig)
        if triplet != "":
            # find five-character sequence in next 1000 hashes
            quintuplet = triplet[0] * 5
            if has_quintuplet(salt, index + 1, quintuplet):
                result.append((index, sig))

        index += 1

    print(result[63][0])



main()
