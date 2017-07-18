# Advent of Code 2016: Day 10, Part 1
# Gregor Ulm


# graph with robot instructions and values they process
g       = dict()

# key: bot, val: value_1, value_2
bots    = dict()

# k: output bin, v: list of values
outputs = dict()



def processBots(to_check):

    if to_check == []:
        return

    # take the first bot in the list and process it
    bot  = to_check.pop()
    vals = bots[bot]

    (high_val, low_val) = (vals["value_1"], vals["value_2"])

    # if bot does not hold two values, skip
    if None in [high_val, low_val]:
        return processBots(toCheck)


    # ensure correct order of values
    if low_val > high_val:
        (low_val, high_val) = (high_val, low_val)

    # remove values from 'bots' dictionary
    bots[bot]["value_1"] = None
    bots[bot]["value_2"] = None

    (give_low,  x1 ) = g[bot]["low"]
    (give_high, x2 ) = g[bot]["high"]

    # update graph to record which value a bot processes
    g[bot]["low"]  = (give_low, low_val)
    g[bot]["high"] = (give_high, high_val)


    # update bot dict by passing on values
    for (b, v) in [(give_low, low_val), (give_high, high_val)]:

            if b.startswith("output"):

                if b in outputs.keys():
                    outputs[b].append(v)
                else:
                    outputs[b] = [v]
                continue

            if b not in bots.keys():
                bots[b] = {"value_1": None, "value_2": None}

            tmp = bots[b]

            if tmp["value_1"] == None:
                bots[b]["value_1"] = v
            elif tmp["value_2"] == None:
                bots[b]["value_2"] = v
                to_check.append(b)


    return processBots(to_check)



def main():

    f    = open("input")
    data = f.readlines()

    # list of tuples: (bot, value)
    instructions = []

    for line in data:
        line = line.strip()

        if line.startswith("value"):
            # e.g. "value 5 goes to bot 2"
            tmp   = line.split(" ")
            value = int(tmp[1])
            bot   = tmp[4] + " " + tmp[5]

            instructions.append((bot, value))

        elif line.startswith("bot"):
            # e.g. "bot 2 gives low to bot 1 and high to bot 0"
            tmp       = line.split(" ")
            bot_in    = tmp[0]  + " " + tmp[1]
            give_low  = tmp[5]  + " " + tmp[6]
            give_high = tmp[10] + " " + tmp[11]

            assert bot_in not in g.keys()
            g[bot_in] = {"high" : (give_high, None),
                         "low"  : (give_low , None)}

            for s in [give_low, give_high]:
                if s.startswith("output"):
                    if s not in outputs.keys():
                        outputs[s] = []


    to_process = []
    for (bot, val) in instructions:
        if bot not in bots.keys():
            bots[bot] = {"value_1": val, "value_2": None}
        else:
            bots[bot]["value_2"] = val
            to_process.append(bot)

    processBots(to_process)


    # find bot that compares 17 and 61:
    for b in g.keys():
        (_, low ) = g[b]["low"]
        (_, high) = g[b]["high"]
        if low == 17 and high == 61:
            print(b)


main()

