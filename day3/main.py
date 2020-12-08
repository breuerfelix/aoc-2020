with open('input.txt') as f:
    data = f.read().split('\n')

ride = []
for line in data:
    if line == '':
        continue

    line_data = [1 if c == '#' else 0 for c in line]
    ride.append(line_data)


def calc(ride, y_factor, x_factor):
    trees, x, y = 0, 0, 0

    while y < len(ride):
        trees += ride[y][x % len(ride[0])]
        y += y_factor
        x = int(y * x_factor)

    return trees

trees1 = calc(ride, 1, 1)
trees2 = calc(ride, 1, 3)
trees3 = calc(ride, 1, 5)
trees4 = calc(ride, 1, 7)
trees5 = calc(ride, 2, .5)

print(trees1 * trees2 * trees3 * trees4 * trees5)
