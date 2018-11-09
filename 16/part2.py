# Advent of Code 2016: Day 16, Part 2
# Gregor Ulm


def checksum(xs):
  acc = []
  while len(xs) > 0:
    first  = xs[0]
    second = xs[1]
    xs     = xs[2:]
    if first == second:
      acc += '1'
    else:
      acc += '0'
  return "".join(acc)


def top(xs):
  i = 0
  while len(xs) % 2 == 0:
    print("i: ", i)
    xs = divide(xs)
    i += 1
  return xs


def divide(xs):
  if (len(xs) % 4) == 0: # input to 'checksum' has to be of even length
    mid = len(xs) // 2
    return divide(xs[:mid]) + divide(xs[mid:])
  else:
    return checksum(xs) # conquer


if __name__ == "__main__":

  # example:
  #(data, goal) = '10000', 20
  # result: 01100

  # provided input (part 1):
  #(data, goal) = '00111101111101000', 272
  # result: 10011010010010010

  # provided input (part 2):
  (data, goal) = '00111101111101000', 35651584
  # Note that the goal is equal to 17 * 2 ^ 21, which hints at
  # divide and conquer.

  # result: 10101011110100011

  inp = data
  l   = len(data)

  while l < goal:

    # reverse:
    data = data[::-1]
    data = int(data,2)

    # flipping the bits:
    ones    = int('1' * l, 2)
    flipped = bin(data ^ ones)[2:] # slicing removes the leading '0b'

    # pad potentially missing zeroes to the left:
    padded = '0' * (l - len(flipped)) + flipped

    # update data:
    data = inp + '0' + padded
    inp  = data
    l    = len(data)

  truncated = data[:goal]
  x = top(truncated)
  print("Checksum: ", x)
