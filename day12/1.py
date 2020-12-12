with open('input.txt') as f:
    data = f.read().split('\n')

data = [x for x in data if x != '']

facing = 'E'
facing_num = 90

x = 0
y = 0

for act in data:
    a = act[0]
    num = int(act[1:])

    direction = a

    if a in ('L', 'R'):
        if a == 'R':
            facing_num += int(num)
            facing_num = (int(facing_num / 90) % 4) * 90

        if a == 'L':
            temp = (int(int(num) / 90) % 4) * 90
            facing_num -= temp
            if facing_num < 0:
                facing_num = 360 + facing_num

        if facing_num == 0:
            facing = 'N'

        if facing_num == 90:
            facing = 'E'

        if facing_num == 180:
            facing = 'S'

        if facing_num == 270:
            facing = 'W'

        continue

    if a == 'F':
        direction = facing

    if direction == 'N':
        y += num

    if direction == 'S':
        y -= num

    if direction == 'W':
        x -= num

    if direction == 'E':
        x += num


print(abs(x) + abs(y))
