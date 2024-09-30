with open('input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file]


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def count_trees(slope):
    right, down = slope
    trees_encountered = 0
    width = len(lines[0])
    height = len(lines)

    x, y = 0, 0

    while y < height:
        if lines[y][x % width] == '#':
            trees_encountered += 1
        x += right
        y += down

    return trees_encountered

tree_counts = [count_trees(slope) for slope in slopes]

result = 1
for count in tree_counts:
    result *= count

print(f"Product of trees encountered: {result}")
