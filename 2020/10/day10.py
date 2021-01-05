ADAPTERS = []
diff_1 = 0
diff_3 = 0

with open("input.txt", "r") as fp:
  for line in fp.readlines():
    if line != '\n':
      ADAPTERS.append(int(line))

ADAPTERS.append(0)
ADAPTERS.sort()
ADAPTERS.append(ADAPTERS[-1]+3)

#for i in range(0, len(ADAPTERS)-1):
#  if ADAPTERS[i+1] - ADAPTERS[i] == 1:
#    diff_1 += 1
#  if ADAPTERS[i+1] - ADAPTERS[i] == 3:
#    diff_3 += 1
#print(f"{diff_1} x {diff_3} = {diff_1*diff_3}")

# i made dis :)
def memoize(func):
    cache = dict()

    def memoized_func(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return memoized_func

@memoize
def combo_count(a: int = 0):

  count = 0

  if a == ADAPTERS[-1]:
    return count + 1

  for ai in [a+i for i in range(1,4) if a+i in ADAPTERS]:
    count += combo_count(ai)

  return count

print(f"count: {combo_count()}")
