with open('input.txt') as f:
    data = f.read().split('\n')

d = [x for x in data if x != '']

# part 1
def run(data):
    excuted_lines = set()

    index = 0
    acc = 0
    finished = False
    while 1:
        if index >= len(data):
            finished = True
            break

        if index in excuted_lines:
            break

        excuted_lines.add(index)

        st = data[index]
        parsed = st.split(' ')
        op = parsed[0]
        val = int(parsed[1])

        if op == 'acc':
            acc += val
        elif op == 'jmp':
            index += val
            continue

        index += 1

    return acc, finished


# part 2
for i, line in enumerate(d):
    if 'jmp' not in line:
        continue

    data = d.copy()
    data[i] = 'nop +0'

    acc, finished = run(data)
    if not finished:
        continue

    print('finished')
    print('acc:', acc)
    print('index:', i)
    break
