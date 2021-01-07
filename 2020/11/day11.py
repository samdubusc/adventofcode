CHART = []

with open("input.txt", "r") as fp:
  for line in fp.readlines():
    if line != '\n':
      CHART.append(list(line))

def check_chart():
  new = []
  for i in range(0, len(CHART)):
    new.append([])
    for j in range(0, len(CHART[0])):
      new[i].append(check_cell(i,j))
  return new

def check_cell(row, col):
  if CHART[row][col] == 'L' and count_visible(row, col) == 0:
    return '#'
  #if CHART[row][col] == '#' and count_neighbors(row, col) >= 4:
  if CHART[row][col] == '#' and count_visible(row, col) >= 5:
    return 'L'
  return CHART[row][col]

def count_neighbors(row, col):
  count = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if row+i == row and col+j == col:
        continue
      if is_inbounds(row+i, col+j) and CHART[row+i][col+j] == '#':
        count += 1
  return count

# ¯\_(ツ)_/¯
def count_visible(row, col):
  count = 0

  # Looking up
  for i in range(1, row+1):
    if CHART[row-i][col] == 'L':
      break
    if CHART[row-i][col] == '#':
      count += 1
      break

  # Looking down
  for i in range(1, len(CHART)-row):
    if CHART[row+i][col] == 'L':
      break
    if CHART[row+i][col] == '#':
      count += 1
      break

  # Looking left
  for i in range(1, col+1):
    if CHART[row][col-i] == 'L':
      break
    if CHART[row][col-i] == '#':
      count += 1
      break

  # Looking right
  for i in range(1, len(CHART[0])-col):
    if CHART[row][col+i] == 'L':
      break
    if CHART[row][col+i] == '#':
      count += 1
      break

  # Looking up+left
  for i in range(1, (row+1 if row+1 < col+1 else col+1)):
    if CHART[row-i][col-i] == 'L':
      break
    if CHART[row-i][col-i] == '#':
      count += 1
      break

  # Looking up+right
  for i in range(1, (row+1 if row+1 < len(CHART[0])-col else len(CHART[0])-col)):
    if CHART[row-i][col+i] == 'L':
      break
    if CHART[row-i][col+i] == '#':
      count += 1
      break

  # Looking down+left
  for i in range(1, len(CHART)-row if len(CHART)-row < col+1 else col+1):
    if CHART[row+i][col-i] == 'L':
      break
    if CHART[row+i][col-i] == '#':
      count += 1
      break

  # Looking down+right
  for i in range(1, len(CHART)-row if len(CHART)-row < len(CHART[0])-col else len(CHART[0])-col):
    if CHART[row+i][col+i] == 'L':
      break
    if CHART[row+i][col+i] == '#':
      count += 1
      break

  return count

def is_inbounds(row, col):
  if row < 0 or row == len(CHART):
    return False
  if col < 0 or col == len(CHART[0]):
    return False
  return True

def pretty_print(chart):
  for i in range(0, len(chart)):
    line = ""
    for j in range(0, len(chart[0])):
      if chart[i][j] != '\n':
        line += chart[i][j]
    print(line)
  print()

def count_occupied(chart):
  count = 0
  for i in range(0, len(CHART)):
    for j in range(0, len(CHART[0])):
      if CHART[i][j] == '#':
        count += 1
  return count

while(True):
  #pretty_print(CHART)  
  new = check_chart()
  if CHART == new:
    print(count_occupied(CHART))
    break
  else:
    CHART = new
