import numpy as np

grid = []
with open('input', 'r') as file:
    lines = file.read().split('\n')

print(lines)
for line in lines:
    row = [int(x) for x in line]
    grid.append(row)

part_1_score = 0
#
grid = np.array(grid)
for idx, row in enumerate(grid):
    for idx2, col in enumerate(row):
        if idx == 0:
            part_1_score += 1
        elif idx == len(grid) - 1:
            part_1_score += 1
        elif idx2 == 0:
            part_1_score += 1
        elif idx2 == len(row) - 1:
            part_1_score += 1
        else:
            max_left = max(grid[idx, :idx2])
            max_right = max(grid[idx, idx2 + 1:])
            max_up = max(grid[:idx, idx2])
            max_down = max(grid[idx + 1:, idx2])

            if col > max_left or col > max_right or col > max_up or col > max_down:
                part_1_score += 1
print(part_1_score)

part_2_score = 0

for i in range(len(grid)):
    for j in range(len(grid[:])):
        score = 1
        base = grid[i, j]
        traversal_score = 0
        # left
        for el in range(j - 1, -1, -1):
            tree = grid[i][el]
            traversal_score += 1
            if tree >= base:
                break
        score *= traversal_score
        traversal_score = 0

        # right
        for el in range(j + 1, len(grid[:])):
            tree = grid[i][el]
            traversal_score += 1
            if tree >= base:
                break
        score *= traversal_score
        traversal_score = 0

        # up
        for el in range(i - 1, -1, -1):
            tree = grid[el][j]
            traversal_score += 1
            if tree >= base:
                break
        score *= traversal_score
        traversal_score = 0

        # down
        for el in range(i + 1, len(grid)):
            tree = grid[el][j]
            traversal_score += 1
            if tree >= base:
                break
        score *= traversal_score
        traversal_score = 0

        if score > part_2_score:
            part_2_score = score

print(part_2_score)
