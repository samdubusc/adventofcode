number = 0
big_number = 0
numbers = []
all_numbers = []

with open("input.txt", "r") as fp:
  for line in fp.readlines():
    if line != '\n':
      all_numbers.append(int(line))
      if len(numbers) < 25:
        numbers.append(int(line))
      else:
        number = int(line)

        in_numbers = False
        for n in numbers:
          if number-n in numbers:
            in_numbers = True
            break

        if not in_numbers:
          big_number = number
          print(f"Number: {number}")

        numbers.append(number)
        numbers.pop(0)

for i in range(0, len(all_numbers)):
  contig = []
  number_sum = all_numbers[i]
  contig.append(all_numbers[i])
  for j in range(1,len(all_numbers)-i):
    contig.append(all_numbers[i+j])
    number_sum += all_numbers[i+j]
    if number_sum > big_number:
      break
    if number_sum == big_number:
      contig.sort()
      print(f"Sum: {contig[0]+contig[-1]}")
      break
