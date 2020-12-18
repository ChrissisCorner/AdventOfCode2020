with open('day04.txt') as f:
    passports_split = f.read().split('\n\n')

passports = []
for p in passports_split:
    passports.append(p.replace('\n', ' ').split(' '))

ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid_passports = 0
passports_final = []
for p in passports:
    d = dict(i.split(':') for i in p)
    passports_final.append(d)

for p in passports_final:
    if 'byr' in p.keys():
        print(p.get('byr'))
        if 1920 <= int(p.get('byr')) and int(p.get('byr')) <= 2002:
            print('passed')
            if 'iyr' in p.keys():
                print('iyr: ', p.get('iyr'))
                if 2010 <= int(p.get('iyr')) and int(p.get('iyr')) <= 2020:
                    print('passed 2')
                    if 'eyr' in p.keys():
                        print('eyr: ', p.get('eyr'))
                        if 2010 <= int(p.get('eyr')) and int(p.get('eyr')) <= 2030:
                            print('passed 3')
                            if 'hgt' in p.keys():
                                print(p.get('hgt'))
                                measure = p.get('hgt')[-2:]
                                value = p.get('hgt')[:-2]

                                if measure == 'in':
                                    print('in')
                                    if  59 <= int(value) and int(value) <= 76:
                                        print('passed 4 -in')
                                        if 'hcl' in p.keys():
                                            print('hcl: ', p.get('hcl'))
                                            #print(p.get('hcl')[:0])
                                            #print(p.get('hcl')[:1])
                                            if p.get('hcl')[:1] == '#':
                                                print('passed #')
                                                print('hcl: ', p.get('hcl')[1:])
                                                if p.get('hcl')[1:].isalnum() and len(p.get('hcl')[1:]) == 6:
                                                    print('passed 5')
                                                    if 'ecl' in p.keys():
                                                        if p.get('ecl') in ecl:
                                                            print('passed 6')
                                                            if 'pid' in p.keys():
                                                                pid = p.get('pid')
                                                                if len(pid) is 9:
                                                                    print('length 9')
                                                                    print(pid[:1])
                                                                    if pid[:1] == '0':
                                                                        print('passed 7')
                                                                        valid_passports += 1

                                elif measure == 'cm':
                                    print('cm')
                                    if 150 <= int(value) and int(value) <= 193:
                                        print('passed 4 -cm')
                                        if 'hcl' in p.keys():
                                            print('hcl: ', p.get('hcl'))
                                            # print(p.get('hcl')[:0])
                                            # print(p.get('hcl')[:1])
                                            if p.get('hcl')[:1] == '#':
                                                print('passed #')
                                                print('hcl: ', p.get('hcl')[1:])
                                                if p.get('hcl')[1:].isalnum() and len(p.get('hcl')[1:]) == 6:
                                                    print('passed 5')
                                                    if 'ecl' in p.keys():
                                                        if p.get('ecl') in ecl:
                                                            print('passed 6')
                                                            if 'pid' in p.keys():
                                                                pid = p.get('pid')
                                                                if len(pid) is 9:
                                                                    print('length 9')
                                                                    print(pid[:1])
                                                                    if pid[:1] == '0':
                                                                        print('passed 7')
                                                                        valid_passports += 1
print('Number passports', valid_passports)

