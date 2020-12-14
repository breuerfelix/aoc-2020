import re

with open('input.txt') as f:
    data = f.read().split('\n')

data = [x for x in data if x != '']

memory = dict()
mask = None

for line in data:
    if 'mask' in line:
        mask = line[7:]
        continue

    pointer, value = re.findall(r'\d+', line)
    pointer = int(pointer)
    value = int(value)

    binary = list('{0:036b}'.format(value))

    for i, c in enumerate(mask):
        if c == 'X':
            continue

        binary[i] = c

    new_value = int(''.join(binary), 2)
    memory[pointer] = new_value

res = 0
for k, v in memory.items():
    res += v

print('part1:', res)

memory = dict()
mask = None


def floating(start, binary, value):
    global memory
    global mask

    for i in range(start, len(mask)):
        if mask[i] != 'X':
            continue

        for val in ['0', '1']:
            binary[i] = val
            floating(i + 1, binary, value)

        return

    new_value = int(''.join(binary), 2)
    memory[new_value] = value


for line in data:
    if 'mask' in line:
        mask = line[7:]
        continue

    pointer, value = re.findall(r'\d+', line)
    pointer = int(pointer)
    value = int(value)

    binary = list('{0:036b}'.format(pointer))

    # apply mask
    for i, c in enumerate(mask):
        if c == '1':
            binary[i] = c

        if c == 'X':
            binary[i] = '0'

    floating(0, binary, value)


res = 0
for k, v in memory.items():
    res += v

print('part2:', res)
