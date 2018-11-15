# Advent of Code 2016: Day 18, Part 1
# Gregor Ulm

def next_row(s):
  padded = '.' + s + '.'
  acc    = ""
  for i in range(1, len(padded) - 1):
    x = padded[i-1:i+2]
    if   x == "^^." : acc += '^'
    elif x == ".^^" : acc += '^'
    elif x == "^.." : acc += '^'
    elif x == "..^" : acc += '^'
    else            : acc += '.'
  return acc


if __name__ == "__main__":

# test cases:
#
#  row   = "..^^."
#  n     = 3
#
#  row   = ".^^.^.^^^^"
#  n     = 10

  f   = open("input")
  row = f.readlines()[0].strip()
  n   = 40
  # result: 1978

  count = 0

  while n > 0:
    count += row.count('.')
    row    = next_row(row)
    n     -= 1

  print("Total: ", count)
