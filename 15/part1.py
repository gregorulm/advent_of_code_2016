# Advent of Code 2016: Day 15, Part 1
# Gregor Ulm


# moves entire array n ticks forward
def tick_new(n, xs_num, xs):

  xs = list(map(lambda x: x + n, xs))

  for i in range(len(xs)):
    xs[i] += i + 1

  acc = []
  for (x, y) in zip(xs_num, xs):
    acc.append(y % x)

  return acc



if __name__ == "__main__":

  """
  # Test case:
  xs_num = [5, 2]
  xs     = [4, 1]
  # Answer: 5
  """

  xs_num = [5, 13, 17, 3, 19, 7]
  xs     = [2, 7, 10, 2, 9, 0]
  # Answer: 148737

  n = 0
  while True:
    if sum(tick_new(n, xs_num, xs)) == 0:
      print("Steps needed: ", n)
      exit()

    else:
      n += 1
