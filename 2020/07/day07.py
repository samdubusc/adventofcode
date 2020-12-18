import re
import networkx

bag_regex = re.compile('(.+) bag[s]* contain (.+ bag[s]*)')
bags_regex = re.compile('(\d) (.+) bag[s]*')
total = 0

DG = networkx.DiGraph()

def traverse_graph(graph, node, weight):
  children = list(graph.successors(node))

  if not children:
    return weight
  else:
    for c in children:
      weights_mult = weight * graph[node][c]['weight']
      c_weight = traverse_graph(graph, c, weights_mult)

      global total
      total += c_weight
    return weight

with open("input.txt", "r") as fp:
  for line in fp.readlines(): 
    if line != "\n":
      bag = bag_regex.match(line).group(1)
      DG.add_node(bag)

      bags = bag_regex.match(line).group(2)
      for b in bags.split(', '):
        if bags_regex.match(b):
          number = bags_regex.match(b).group(1)
          name = bags_regex.match(b).group(2)
          DG.add_weighted_edges_from([(bag, name, int(number))])

traverse_graph(DG, 'shiny gold', 1)
print(total)
