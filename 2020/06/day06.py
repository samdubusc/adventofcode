group = {}
total = 0
group_size = 0

with open("input.txt", "r") as fp:
  for line in fp.readlines():
    line = line.rstrip()
    if (line == ""):
      for key, value in group.items():
        if value == group_size:
          total += 1
      group = {}
      group_size = 0
    else:
      group_size += 1
      for c in line:
        if c not in group:
          group[c] = 1
        else:
          group[c] += 1

  print(total)
