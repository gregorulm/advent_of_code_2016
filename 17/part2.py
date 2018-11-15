# Advent of Code 2016: Day 17, Part 2
# Gregor Ulm

import hashlib


def get_hash(s):
  return hashlib.md5(s.encode('utf-8')).hexdigest()


# filtering out steps that can't be taken due to blocked doors, i.e.
# possible directions are mapped to corresponding positions in the grid
def valid_steps(ds, steps):
  acc = []
  for (d, (x, y)) in steps:
    if d in ds:
      acc.append((d, (x, y)))
  return acc


# legal in the matrix, ignoring locked doors
def legal_steps(pos):
  (x, y)     = pos
  acc        = []
  candidates = [(x - 1, y), (x + 1, y), (x, y -1 ), (x, y + 1)]
  #             ^ left      ^ right      ^ up        ^ down
  for ((m, n), d) in zip(candidates, ['L', 'R', 'U', 'D']):
    if m >= 0 and m <= 3:
      if n >= 0 and n <= 3:
        acc.append((d, (m, n)))
  return acc


# directions possible based on input
def directions(s):
  s     = s[:4] # retain only the first four characters
  acc   = []
  chars = "bcdef"
  for (i, c) in zip([0, 1, 2, 3], ['U', 'D', 'L', 'R']):
    if s[i] in chars:
      acc.append(c)
  return acc



if __name__ == "__main__":

  states   = []
  longest  = None

  # examples
  # phrase = "ihgpwlah" # 370
  # phrase = "kglvqrro" # 492
  # phrase = "ulqzkmiv" # 830
  phrase = "pslxynzg" # 488

  data = (phrase, (0, 0), "") # code, pos, path
  states.append(data)

  while True:

    if states == []:
      print("No valid path left. Exiting.")
      break

    val = states.pop()

    code = val[0]
    pos  = val[1]
    path = val[2]

    if pos == (3, 3): # we are done!
      if longest == None or longest < len(path):
        longest = len(path)
        print("Success! Length:", len(path))
      continue

    ds = directions(get_hash(code + path))
    ps = legal_steps(pos)
    vs = valid_steps(ds, ps)

    for (d, xy) in vs:
      states.append((code, xy, path + d))

  print("Length of longest path:", longest)
