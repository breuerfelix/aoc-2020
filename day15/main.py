with open('input.txt') as f:
    data = f.read().split('\n')[0].split(',')

data = [int(x) for x in data]

i = 2
last_number = data[0]
spoken = data[0]
mem = dict()

while 1:
    if i <= len(data):
        mem[last_number] = i - 1
        spoken = data[i - 1]
        last_number = spoken
        i += 1
        continue

    if last_number not in mem:
        spoken = 0
    else:
        spoken = (i - 1) - mem[last_number]

    # save the number
    mem[last_number] = i - 1

    last_number = spoken
    i += 1

    if i > 30000000:
        break


print('last spoken:', spoken)
