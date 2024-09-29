with open('input.txt', 'r') as file:
  # Line List
  lines:list = [line.strip() for line in file]
valid:int = 0
for line in lines:
  splitted_array:list = line.split()
  splitted_numbers:list = splitted_array[0].split("-")
  lower_limit:int = int(splitted_numbers[0])
  upper_limit:int = int(splitted_numbers[1])
  character:str = splitted_array[1].split(":")[0]
  occurance:int = splitted_array[2].count(character)
  if occurance>=lower_limit and occurance<=upper_limit:
    valid+=1
print(valid)

