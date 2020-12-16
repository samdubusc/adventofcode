import re

total = 0

def validate(key, value):
  if (key == "byr" and 1920 <= int(value) <= 2020 ):
    return True
  if (key == "iyr" and 2010 <= int(value) <= 2020):
    return True
  if (key == "eyr" and 2020 <= int(value) <= 2030):
    return True
  if (key == "hgt"):
    p = re.compile('(\d+)(cm|in)')
    if (bar := p.match(value)):
      if (bar.group(2) == "cm" and 150 <= int(bar.group(1)) <= 193):
        return True
      if (bar.group(2) == "in" and 59 <= int(bar.group(1)) <= 76):
        return True 
  if (key == "hcl"):
    p = re.compile('#[0-9a-f]{6}')
    if p.match(value) != None:
      return True
  if (key == "ecl"):
    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
      return True
  if (key == "pid"):
    p = re.compile('^[0-9]{9}$')
    if p.match(value) != None:
      return True
  if (key == "cid"):
    return True

  return False

with open("input.txt", "r") as fp:
  key_values = []
  req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  for line in fp.readlines():
    if (line == "\n"):
      foo = dict(key_values)
      all_good = True
      for key in req_keys:
        if key not in foo:
          all_good = False
          break
        else:
          if validate(key, foo[key]) == False:
            print(f'value is invalid- {key}:{foo[key]}')
            all_good = False
            break
      if all_good == True:
        total += 1
      key_values = []
    else:
      pairs = line.split(' ')
      for pair in pairs:
        key_values.append(pair.rstrip().split(':'))

print(total)
