import math

with open('input.txt') as f:
    data = f.read().split('\n')

data = [x for x in data if x != '']

x = 10
y = 1

ship_x = 0
ship_y = 0


def rotate(origin, point, angle):
    # stole that from stackoverflow ...
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


for act in data:
    a = act[0]
    num = int(act[1:])

    direction = a

    if a in ('L', 'R'):
        num = int(num)
        if a == 'R':
            num = -num

        x, y = rotate((0, 0), (x, y), math.radians(num))
        x = round(x)
        y = round(y)
        continue

    if a == 'F':
        # move ship
        ship_x += int(num) * x
        ship_y += int(num) * y
        continue

    if direction == 'N':
        y += num

    if direction == 'S':
        y -= num

    if direction == 'W':
        x -= num

    if direction == 'E':
        x += num


print(abs(ship_x) + abs(ship_y))
