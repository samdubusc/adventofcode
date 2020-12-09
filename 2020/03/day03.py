with open("input.txt", "r") as fp:
  counter = 1
  total = 1
  paths = [
    {"r": 1, "d": 1, "i" : 0, "c": 0},
    {"r": 3, "d": 1, "i" : 0, "c": 0},
    {"r": 5, "d": 1, "i" : 0, "c": 0},
    {"r": 7, "d": 1, "i" : 0, "c": 0},
    {"r": 1, "d": 2, "i" : 0, "c": 0},
  ]
  fp.readline()
  for line in fp.readlines():
    for p in paths:
      if counter % p["d"] == 0:
        p["i"] += p["r"]
        if line[(p["i"]) % (len(line)-1)] == '#':
          p["c"] += 1
    counter += 1

  for p in paths:
    total *= p["c"]

  print(total)
