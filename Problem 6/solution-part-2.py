import re

def is_valid(passport):
    if not (1920 <= int(passport.get('byr', 0)) <= 2002):
        return False

    if not (2010 <= int(passport.get('iyr', 0)) <= 2020):
        return False

    if not (2020 <= int(passport.get('eyr', 0)) <= 2030):
        return False

    hgt = passport.get('hgt', '')
    if 'cm' in hgt:
        if not (150 <= int(hgt.replace('cm', '')) <= 193):
            return False
    elif 'in' in hgt:
        if not (59 <= int(hgt.replace('in', '')) <= 76):
            return False
    else:
        return False

    if not re.match(r"^#[0-9a-f]{6}$", passport.get('hcl', '')):
        return False

    if passport.get('ecl', '') not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if not re.match(r"^\d{9}$", passport.get('pid', '')):
        return False
    return True

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

valid_passport_count = 0
passport_data = {}

for item in lines:
    if item:
   
        fields = item.split()
        for field in fields:
            key, value = field.split(':')
            passport_data[key] = value
    else:
      
        if all(field in passport_data for field in ['byr','iyr','eyr','hgt','hcl','ecl','pid']) and is_valid(passport_data):
            valid_passport_count += 1

        passport_data = {}


if all(field in passport_data for field in ['byr','iyr','eyr','hgt','hcl','ecl','pid']) and is_valid(passport_data):
    valid_passport_count += 1

print(valid_passport_count)
