with open('input.txt') as f:
    data = f.read().split('\n')

def binary(string, lower, upper, mi, ma):
    for c in string:
        half = int((ma - mi) / 2)

        if c == lower:
            ma = half + mi
        elif c == upper:
            mi = half + mi

    return ma


highest = 0
id_list = set()
for seat in data:
    if seat == '':
        continue

    row = binary(seat[:7], 'F', 'B', 0, 127)
    seat = binary(seat[-3:], 'L', 'R', 0, 7)

    ID = (row * 8) + seat
    id_list.add(ID)
    if ID > highest:
        highest = ID

print(highest)

free = set()
for i in range(127):
    for ii in range(7):
        temp_id = (i * 8) + ii
        if temp_id in id_list:
            continue

        if (temp_id + 1) not in id_list:
            continue

        if (temp_id - 1) not in id_list:
            continue

        free.add(temp_id)



print(free)
