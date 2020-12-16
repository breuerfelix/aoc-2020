import re

with open('input.txt') as f:
    data = f.read().split('\n')

rules = """
departure location: 30-260 or 284-950
departure station: 29-856 or 863-974
departure platform: 32-600 or 611-967
departure track: 44-452 or 473-965
departure date: 36-115 or 129-950
departure time: 50-766 or 776-972
arrival location: 40-90 or 104-961
arrival station: 40-864 or 887-971
arrival platform: 32-920 or 932-964
arrival track: 45-416 or 427-959
class: 47-536 or 557-964
duration: 33-229 or 246-969
price: 25-147 or 172-969
route: 32-328 or 349-970
row: 50-692 or 709-964
seat: 49-292 or 307-964
train: 28-726 or 748-954
type: 37-430 or 438-950
wagon: 46-628 or 638-973
zone: 39-786 or 807-969
"""
# rules = """
# class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19
# """

rules = [x for x in rules.split('\n') if x != '']

my_ticket = '89,193,59,179,191,173,61,73,181,67,71,109,53,79,83,113,107,139,131,137'
my_values = [int(x) for x in my_ticket.split(',')]

nearby_tickets = [[int(i) for i in x.split(',')] for x in data if x != '']

rules_dict = dict()
for rule in rules:
    name, values = rule.split(':')

    rules_dict[name] = list()

    for pair in values.split('or'):
        min_val, max_val = re.findall(r'\d+', pair)
        rules_dict[name].append((int(min_val), int(max_val)))


def check(value):
    pos = set()
    for k, val in rules_dict.items():
        for min_val, max_val in val:
            if value >= min_val and value <= max_val:
                pos.add(k)

    return True if len(pos) > 0 else False, pos

false = 0

valid_tickets = list()
for ticket in nearby_tickets:
    valid = True
    for val in ticket:
        v, _ = check(val)
        if v:
            continue

        valid = False
        false += val

    if valid:
        valid_tickets.append(ticket)

print(false)

# part 2
sets = dict()
for ticket in valid_tickets:
    for i, val in enumerate(ticket):
        _, positions = check(val)

        if i not in sets:
            sets[i] = list()

        sets[i].append(positions)

gone = set()
fields = dict()
while 1:
    item = None
    for i, s in sets.items():
        temp = set.intersection(*s)
        diff = temp.difference(gone)

        if len(diff) == 1:
            item = list(diff)[0]
            gone.add(item)
            fields[i] = item

    if len(fields) == len(sets):
        break

result = 1
for i, val in fields.items():
    if 'departure' not in val:
        continue

    result *= my_values[i]

print(result)
