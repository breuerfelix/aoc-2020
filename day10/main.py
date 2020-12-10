with open('input.txt') as f:
    data = f.read().split('\n')

data = [int(x) for x in data if x != '']
data = set(data)

data.add(0)
phone = max(data) + 3
data.add(phone)

data_list = list(data)

counts = {
    1: 0,
    2: 0,
    3: 0,
}

for i, j in enumerate(data):
    if i == 0:
        continue

    diff = j - data_list[i - 1]
    if diff > 3:
        raise 'diff is greater than 3'

    if diff < 1:
        raise 'diff lower 1'

    counts[diff] += 1

print(counts[1] * counts[3])

# part2
class Node:
    def __init__(self, val):
        self.val = val
        self.leafs = []
        self.temp = None

    def calc(self):
        if self.temp is not None:
            return self.temp

        if len(self.leafs) == 0:
            return 1

        acc = 0
        for l in self.leafs:
            acc += l.calc()

        # remind this solution
        self.temp = acc
        return acc



data = set(data_list)
nodes = dict()
for d in data:
    n = Node(d)
    nodes[d] = n

for i, current in enumerate(data):
    n = nodes[current]

    for maybe in range(1, 4):
        m = current + maybe
        if m not in data:
            continue

        n.leafs.append(nodes[m])


# start reversed with calculation
for r in sorted(list(data), reverse=True):
    nodes[r].calc()

print(nodes[0].temp)
