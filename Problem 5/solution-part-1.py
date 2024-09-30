with open('input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file]

trees_encountered = 0
right = 3
down = 1
width = len(lines[0])
height = len(lines)


x, y = 0, 0

while y < height:
    if lines[y][x % width] == '#':
        trees_encountered += 1
    x += right
    y += down

print(f"Trees Encountered: {trees_encountered}")
