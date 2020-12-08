numbers = {}

with open("input.txt", "r") as fp:
  for line in fp.readlines():
    line = int(line)
    if line in numbers:
      print(numbers[line] * line)

    numbers[2020-line] = line

    for key, value in numbers.items():
      if (line + value) in numbers:
        print(line * value * numbers[line+value])
        break
