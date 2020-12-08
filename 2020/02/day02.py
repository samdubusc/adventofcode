with open("input.txt", "r") as fp:
  numbers = 0
  for line in fp.readlines():
    (indices, char, pw) = line.split( )
    first, second = indices.split('-')
    char = char.strip(':')
    if (pw[int(first)-1] == char) != (pw[int(second)-1] == char):
      numbers += 1

  print(numbers)
