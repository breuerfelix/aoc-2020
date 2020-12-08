with open('input.txt') as f:
    d = f.read().split('\n')

d = [x for x in d if x != '']

rules = dict()
cons = set()

for l in d:
    l = l.replace('.', ', ').replace('g, ', 'gs, ')
    split = l.split(' bags contain ')

    contain = split[1].split(' bags, ')
    contain = [x for x in contain if x != '']

    bag = split[0]

    rules[bag] = dict()

    for c in contain:
        temp = c.split(' ')
        count = temp[0]
        name = ' '.join(temp[1:])
        rules[bag][name] = count

        if name == 'shiny gold':
            cons.add(bag)

while 1:
    old_len = len(cons)
    for name, val in rules.items():
        for k, v in val.items():
            if k in cons:
                cons.add(name)

    if old_len == len(cons):
        break

print(len(cons))

# part 2
def req(key):
    bags = rules[key]
    number = 0
    for k, v in bags.items():
        if v == 'no':
            return 0

        number += int(v)
        number += (int(v) * req(k))

    return number

inside = req('shiny gold')
print(inside)
