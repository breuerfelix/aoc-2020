with open("data2.txt") as f:
    data = f.read().split("\n")

print(data[0])

correct = 0
wrong = 0
for line in data:
    if line == "":
        continue

    split = line.split(" ")
    first = split[0].split("-")
    minimum = int(first[0])
    maximum = int(first[1])
    print(minimum)
    print(maximum)

    char = split[1].split(":")[0]
    print(char)

    word = split[2]
    #print(word)
    #print('len', len(word))

    if len(word) < maximum:
        print('does not match')
        print(word)
        print(maximum)
        continue

    first_occ = word[minimum - 1]
    sec_occ = word[maximum - 1]

    if (first_occ == char) and (sec_occ == char):
        wrong += 1
        continue
    elif (first_occ != char) and (sec_occ != char):
        wrong += 1
        continue
    elif (first_occ == char) and (sec_occ != char):
        correct += 1
        continue
    elif (first_occ != char) and (sec_occ == char):
        correct += 1
        continue


    # counter = 0
    # for c in word:
        # if c == char:
            # counter += 1

    # print(counter)

    # if (counter > maximum) or (counter < minimum):
        # wrong += 1
        # print("wrong")
        # continue
    # elif (counter >= minimum) and (counter <= maximum):
        # correct += 1
        # print("right")
        # continue

    print("shouldnt get here")

    break

print("correct:", correct)
print("wrong:", wrong)
