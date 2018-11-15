# Advent of Code 2016: Day 18, Part 2
# Gregor Ulm

def next_row(s):
  padded = '.' + s + '.'
  acc    = ""
  for i in range(1, len(padded) - 1):
    x = padded[i-1:i+2]
    if x in ["^^.", ".^^", "^..", "..^"]:
      acc += '^'
    else :
      acc += '.'
  return acc



if __name__ == "__main__":
  f   = open("input")
  row = f.readlines()[0].strip()
  n   = 400000
  # result: 20003246
  count = 0

  while n > 0:
    if n % 20000 == 0:
      print("n: ", n)
    count += row.count('.')
    row    = next_row(row)
    n     -= 1

  print("Total: ", count)
