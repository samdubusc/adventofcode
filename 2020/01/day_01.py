f = open("input.txt", "r")

numbers = {}

for line in f:
  line = int(line)
  if line in numbers:
    print(numbers[line] * line)
    break
  else:
    numbers[2020-line] = line

f.close()
