# Advent of Code 2016: Day 16, Part 1
# Gregor Ulm


def checksum(xs):

  acc = []

  while len(xs) > 1:
    first  = xs[0]
    second = xs[1]
    xs     = xs[2:]
    
    if first == second:
      acc += '1'
    else:
      acc += '0'
       
  if len(acc) % 2 == 0:
    return checksum(acc)
    
  return "".join(acc)



if __name__ == "__main__":
  
  # example:
  #(data, goal) = '10000', 20  # result: 01100

  # provided input:
  (data, goal) = '00111101111101000', 272  # result: 10011010010010010
    
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
  x = checksum(truncated)
  print("Checksum: ", x)
