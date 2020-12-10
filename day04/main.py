import re

with open('input.txt') as f:
    data = f.read().split('\n')

parsed = dict()
passports = []
for row in data:
    if row == '':
        passports.append(parsed)
        parsed = dict()
        continue

    entries = row.split(' ')
    for entry in entries:
        key, value = entry.split(':')
        parsed[key] = value

def byr(value):
    val = int(value)
    return (val >= 1920) and (val <= 2002)

def iyr(value):
    val = int(value)
    return (val >= 2010) and (val <= 2020)

def eyr(value):
    val = int(value)
    return (val >= 2020) and (val <= 2030)

def hgt(value):
    unit = value[-2:]
    if (unit != 'cm') and (unit != 'in'):
        return False

    height = int(value[:-2])
    if unit == 'cm':
        return (height >= 150) and (height <= 193)

    if unit == 'in':
        return (height >= 59) and (height <= 76)

    return False

def hcl(value):
    if value[0] != '#':
        return False

    val = value[1:]
    if len(val) != 6:
        return False
    hm = re.search(r'^(?:[0-9a-f]{3}){1,2}$', val)

    if hm is None:
        return False

    return True

def ecl(value):
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for val in valid:
        if val == value:
            return True

    return False

def pid(value):
    if len(value) != 9:
        return False

    return value.isdigit()

required = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid,
}

valid = 0
for passport in passports:
    for field, func in required.items():
        if field in passport:
            if func(passport[field]):
                continue

        break
    else:
        valid += 1

print(valid)
print(len(passports))
