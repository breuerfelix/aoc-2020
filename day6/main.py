with open('input.txt') as f:
    data = f.read().split('\n')

group = set()
groups = list()

for line in data:
    if line == '':
        groups.append(group)
        group = set()
        continue
    for c in line:
        group.add(c)

count = 0
for s in groups:
    count += len(s)

print(count)

unique = set()
unique_list = list()

first = True
for line in data:
    if line == '':
        first = True
        unique_list.append(unique)
        unique = set()
        continue

    if first:
        for c in line:
            unique.add(c)
        first = False
        continue

    to_remove = set()
    for u in unique:
        if u not in line:
            to_remove.add(u)

    for u in to_remove:
        unique.remove(u)

count = 0
for s in unique_list:
    count += len(s)
print(count)
