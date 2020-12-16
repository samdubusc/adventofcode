seat_ids = []
highest_id = 0

with open("input.txt", "r") as fp:
  for line in fp.readlines():
    row = 0
    col = 0
    seat_id = 0
    for i in range(0, len(line)):
      if i <= 6 and line[i] == "B":
        row += 2**(6-i)
      if i > 6 and line[i] == "R":
        col += 2**(9-i)
    seat_id = (row * 8) + col
    seat_ids.append(seat_id)
    if seat_id > highest_id:
      highest_id = seat_id

  seat_ids.sort(reverse = True)
  for i in range(0, len(seat_ids)-1):
    if seat_ids[i] - seat_ids[i+1] == 2:
      print(seat_ids[i+1]+1)
