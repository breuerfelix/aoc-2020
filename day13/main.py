with open('bla.txt') as f:
    data = f.read().split('\n')
# 803025030761664
print(data)
time = int(data[0])
my_time = time

busses = data[1].split(',')

while 1:
    for bus in busses:
        if bus == 'x':
            continue

        t = int(bus)
        if time % t != 0:
            continue

        print('bus:', bus)
        print('time:', time)
        print('result:', (time - my_time) * t)
        break
    else:
        time += 1
        continue

    break

# part2
while 1:
    step = 1
    for i, bus in enumerate(busses):
        if bus == 'x':
            continue

        bus_id = int(bus)
        if (time + i) % bus_id != 0:
            break
        else:
            step *= bus_id
    else:
        # not breaked loop -> found it
        break

    # try again
    time += step
    continue

print('found:', time)
