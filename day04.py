with open('day04.txt') as f:
    passports_split = f.read().split('\n\n')

passports = []
for p in passports_split:
    passports.append(p.replace('\n', ' ').split(' '))

valid_passports = 0
passports_final = []
for p in passports:
    d = dict(i.split(':') for i in p)
    passports_final.append(d)

for p in passports_final:
    if 'byr' in p.keys():
        if 'iyr' in p.keys():
            if 'eyr' in p.keys():
                if 'hgt' in p.keys():
                    if 'hcl' in p.keys():
                        if 'ecl' in p.keys():
                            if 'pid' in p.keys():
                                valid_passports += 1

print(valid_passports)