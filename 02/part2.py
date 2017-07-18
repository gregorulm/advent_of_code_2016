# Advent of Code 2016: Day 2, Part 2
# Gregor Ulm


graph = dict()

# conflict: direction "D" and label "D", thus lowercase for all labels
graph[1]   = {"D": 3}
graph[2]   = {"R": 3, "D": 6}
graph[3]   = {"U": 1, "L": 2, "R": 4, "D": 7}
graph[4]   = {"L": 3, "D": 8}
graph[5]   = {"R": 6}
graph[6]   = {"U": 2, "L": 5, "R": 7, "D": "a"}
graph[7]   = {"U": 3, "L": 6, "R": 8, "D": "b"}
graph[8]   = {"U": 4, "L": 7, "R": 9, "D": "c"}
graph[9]   = {"L": 8}
graph["a"] = {"U": 6, "R": "b"}
graph["b"] = {"U": 7, "L": "a", "R": "c", "D": "d"}
graph["c"] = {"L": "b", "U": 8}
graph["d"] = {"U": "b"}



def main():

    #data = "ULL\nRRDDD\nLURDL\nUUUUD".split()

    f    = open("input")
    data = f.readlines()

    pos  = 5
    code = ""


    for line in data:

        for move in line:

            next_moves = graph[pos].keys()

            if move in next_moves:
                pos = graph[pos][move]
            else:
                continue

        code += str(pos)

    print(code.upper())


main()
