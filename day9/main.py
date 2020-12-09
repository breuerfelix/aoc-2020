with open('input.txt') as f:
    data = f.read().split('\n')

data = [int(x) for x in data if x != '']

preamble = 25
weakness = -1
for i, num in enumerate(data[preamble:]):
    prev = set(data[i:i + preamble])

    found = False
    for k in prev:
        for kk in prev:
            if k == kk: continue
            if (k + kk) == num:
                found = True
                break

        if found: break

    if not found:
        print('weakness:', num)
        weakness = num
        break

index = 0
last_index = 0
sums = []

while 1:
    sums.append(data[index])
    index += 1

    s = sum(sums)
    if s == weakness:
        print('weakness found!', sums)
        print('res:', max(sums) + min(sums))
        break

    if s > weakness:
        sums = []
        index = last_index + 1
        last_index = index
