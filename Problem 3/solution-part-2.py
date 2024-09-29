with open('input.txt', 'r') as file:
  # Line List
  lines:list = [line.strip() for line in file]
valid:int = 0
for line in lines:
  splitted_array:list = line.split()
  splitted_numbers:list = splitted_array[0].split("-")
  first_position:int = int(splitted_numbers[0]) - 1
  second_position:int = int(splitted_numbers[1]) - 1
  character:str = splitted_array[1].split(":")[0]
  try:
    if (splitted_array[2][first_position] == character) ^ (splitted_array[2][second_position] == character):
      valid+=1
  except:
    IndexError("Error occured")
print(valid)

