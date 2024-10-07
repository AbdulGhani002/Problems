with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

necessary_fields = ['ecl','pid','eyr','hcl','byr','iyr','hgt']

valid_passport = 0
new_list = []
for item in lines:
    if item:
        new_list.append(item)
    else:
        passport_data = ' '.join(new_list)
        
        if all(field in passport_data for field in necessary_fields):
            valid_passport += 1
        
        new_list = []

if new_list:
    passport_data = ' '.join(new_list)
    if all(field in passport_data for field in necessary_fields):
        valid_passport += 1

print(valid_passport)
