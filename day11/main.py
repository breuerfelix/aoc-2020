with open('test.txt') as f:
    data = f.read().split("\n")

d = list()
for row in data:
    if row == '':
        continue

    r = list()
    d.append(r)
    for c in row:
        if c == '.':
            r.append(-1)
            continue

        if c == 'L':
            r.append(0)
            continue

        if c == '#':
            r.append(1)
            continue



def check(data, i, ii):
    surround = 0

    if i > 0 and data[i - 1][ii] == 1:
        surround += 1

    if i < len(data) - 1 and data[i + 1][ii] == 1:
        surround += 1

    if ii > 0 and data[i][ii - 1] == 1:
        surround += 1

    if ii < len(data[0]) - 1 and data[i][ii + 1] == 1:
        surround += 1

    if i > 0 and ii > 0 and data[i - 1][ii - 1] == 1:
        surround += 1

    if i < len(data) - 1 and ii < len(data[0]) - 1 and data[i + 1][ii + 1] == 1:
        surround += 1

    if i > 0 and ii < len(data[0]) - 1 and data[i - 1][ii + 1] == 1:
        surround += 1

    if i < len(data) - 1 and ii > 0 and data[i + 1][ii - 1] == 1:
        surround += 1

    return surround

def render(data):
    occ = 0
    for row in data:
        string = ''
        for place in row:
            if place == 1:
                string += '#'
                occ += 1
            if place == 0:
                string += 'L'
            if place == -1:
                string += '.'
        print(string)
    return occ


old = d
counter = 0
while 1:
    new = [x.copy() for x in old]

    changed = 0

    for i, row in enumerate(old):
        for ii, seat in enumerate(row):
            curr = old[i][ii]
            if curr == -1:
                continue

            surr = check(old, i, ii)
            if curr == 0 and surr == 0:
                new[i][ii] = 1
                changed += 1

            if curr == 1 and surr >= 4:
                new[i][ii] = 0
                changed += 1

    old = new
    counter += 1

    if changed == 0:
        break

print('counter:', counter)
occ = render(old)
print('occ:', occ)

# part 2

def check2(data, i, ii):
    # TODO fix this thing
    surround = 0

    # check on the right
    for x in range(ii + 1, len(data[0])):
        if data[i][x] == -1:
            continue

        if data[i][x] == 1:
            surround += 1

        break


    # check on the left
    for x in range(ii - 1, -1, -1):
        if data[i][x] == -1:
            continue

        if data[i][x] == 1:
            surround += 1

        break

    # check on the top
    for x in range(i - 1, -1, -1):
        if data[x][ii] == -1:
            continue

        if data[x][ii] == 1:
            surround += 1

        break

    # check on the bottom
    for x in range(i + 1, len(data)):
        if data[x][ii] == -1:
            continue

        if data[x][ii] == 1:
            surround += 1

        break

    # check diagonal bottom right
    return surround


old = d
counter = 0
while 1:
    new = [x.copy() for x in old]

    changed = 0

    for i, row in enumerate(old):
        for ii, seat in enumerate(row):
            curr = old[i][ii]
            if curr == -1:
                continue

            surr = check2(old, i, ii)
            if curr == 0 and surr == 0:
                new[i][ii] = 1
                changed += 1

            if curr == 1 and surr >= 5:
                new[i][ii] = 0
                changed += 1

    old = new
    counter += 1

    if changed == 0:
        break

occ = render(old)
print('occ:', occ)
print('counter:', counter)
