# Advent of Code 2016: Day 11, Part 1
# Gregor Ulm


from itertools import chain, combinations


# cf. http://stackoverflow.com/questions/374626/
def powerset(iterable):
    xs = list(iterable)
    return chain.from_iterable(combinations(xs,n)
        for n in range(len(xs)+1))



# filters all combinations, returns list of sets
def takeOneOrTwo(xs):

    res = []
    for el in xs:
        if len(el) == 1 or len(el) == 2:
            res.append(set(el))

    return res



# turn dict into string
def dictToString(d):

    # sample output: "1HMLM2HG3LG4_"

    res = ""

    for i in range(1, 5):

        res  += str(i)
        floor = sorted(list(d[i]))

        if floor == []:
            res += "_"

        else:
            for x in floor:
                res += x

    return res



def isValid(elems):
    # verifies validity of arrangement of elements on floor and in elevator

    unpaired_Ms   = set()
    has_generator = False

    for x in elems:
        if x[1] == "M" and ((x[0] + "G") not in elems):
            unpaired_Ms.add(x)

        if x[1] == "G":
            has_generator = True

    if (len(unpaired_Ms) >= 1) and has_generator:
        return False

    return True



def main():

    # test case:
    # The first floor contains a hydrogen-compatible microchip
    #     and a lithium-compatible microchip.
    # The second floor contains a hydrogen generator.
    # The third floor contains a lithium generator.
    # The fourth floor contains nothing relevant.
    """
    floors = { 4 : set()             ,
               3 : {"LG"}            ,
               2 : {"HG"}            ,
               1 : {"HM", "LM"}      }

    elevator = 1
    steps    = 0
    """

    # problem input:
    # The first floor contains
    #        a polonium generator,
    #        a thulium generator,
    #        a thulium-compatible microchip,
    #        a promethium generator,                  # OG
    #        a ruthenium generator,
    #        a ruthenium-compatible microchip,
    #        a cobalt generator,
    #        and a cobalt-compatible microchip.
    #
    #The second floor contains
    #        a polonium-compatible microchip
    #        and a promethium-compatible microchip.   # OM
    #
    #The third floor contains nothing relevant.
    #The fourth floor contains nothing relevant.

    floors = { 4 : set()             ,
               3 : set()            ,
               2 : {"PM", "OM"}            ,
               1 : {"PG", "TG", "TM", "OG", "RG", "RM", "CG", "CM" } }

    elevator = 1
    steps    = 0


    start       = (floors, elevator, steps)
    current_min = 100 # initialize to a comfortably large number
    states      = [start]

    # k: string representing floor configuration, v; current min steps
    cache = dict()

    while not states == []:

        # take one of the states and create all future states for it
        (floors, elevator, steps) = states.pop()

        # check if it is a valid end state, i.e. first three floors empty
        cleared = True
        for i in range(1, 4):
            if len(floors[i]) != 0:
                cleared = False
                break

        if cleared:
            print(floors, elevator, steps)

            if steps < current_min:
                current_min = steps

            continue


        # discard if suboptimal:
        if steps >= current_min:
            continue


        # generate all possible moves
        future_states = []

        # take between 0 and 2 elements from current row
        comb          = takeOneOrTwo(list(powerset(floors[elevator])))
        # filter out invalid item combinations for elevator
        comb          = list(filter(lambda x : isValid(x), comb))


        # one floor up
        if elevator != 4:

            for c in comb:

                new_elevator = elevator + 1
                new_steps    = steps    + 1
                new_floor    = dict()

                for i in range(1, 5):

                    if i == elevator:
                        new_floor[i] = floors[i] - c

                    elif i == elevator + 1:
                        new_floor[i] = floors[i] | c  # set union

                    else:
                        new_floor[i] = floors[i]

                future_states.append((new_floor, new_elevator, new_steps))


        # one floor down
        if elevator != 1:

           for c in comb:

            # it's not a good idea to take two elements down a floor
            if len(c) == 2:
                continue

            else:
                new_elevator = elevator - 1
                new_steps    = steps    + 1
                new_floor    = dict()

                for i in range(1, 5):

                    if i == elevator:
                        new_floor[i] = floors[i] - c

                    elif i == elevator - 1:
                        new_floor[i] = floors[i] | c  # set union

                    else:
                        new_floor[i] = floors[i]

                future_states.append((new_floor, new_elevator, new_steps))


        # discard all invalid states
        valid_states = []

        for (floors, elevator, steps) in future_states:

            valid = True

            for i in range(1, 5):

                if not isValid(floors[i]):
                    valid = False
                    break


            if valid:
                # check if in cache
                k = (dictToString(floors) + str(elevator))

                if k not in cache.keys():
                    cache[k] = steps
                    valid_states.append((floors, elevator, steps))

                else:
                    if steps < cache[k]:
                        cache[k] = steps
                        valid_states.append((floors, elevator, steps))

        states = valid_states + states

    print("Min steps: ", current_min)



main()


