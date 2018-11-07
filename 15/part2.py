# Advent of Code 2016: Day 15, Part 2
# Gregor Ulm

"""
Note that the code in part1.py is perfectly adequate for determining
the correct solution within a few seconds. As an exercise, I made a
few minor changes to it that speed it up.
"""

# moves entire array n ticks forward and checks if the resulting
# configuration of disks is valid
def valid(n, xs_num, xs):
  for i in range(len(xs)):
    x = xs_num[i]
    y = xs[i] + n + i + 1
    if (y % x) != 0:
      return False
  return True



if __name__ == "__main__":

  """
  # Test case:
  xs_num = [5, 2]
  xs     = [4, 1]
  # Answer: 5
  """

  xs_num = [5, 13, 17, 3, 19, 7, 11]
  xs     = [2, 7, 10, 2, 9, 0, 0]
  # Answer: 2353212

  n = 0
  while True:
    if valid(n, xs_num, xs):
      print("Steps needed: ", n)
      exit()
    n += 1
