import numpy as np

with open('input.txt', 'r') as file:
    lines = file.read().split("\n")

ROCK = "#"
AIR = "."
SAND = "o"


def construct_rock_lines(x1, y1, x2, y2):
    x_line = range(x1, x2 + 1) if x1 < x2 else (range(x2, x1 + 1))
    y_line = range(y1, y2 + 1) if y1 < y2 else (range(y2, y1 + 1))

    rock_lines = [(x,y) for x in x_line for y in y_line]
    return rock_lines


map = np.full((1000, 1000), AIR)
max_depth = 0

for line in lines:
    path = line.split(' -> ')
    for i in range(len(path) - 1):
        x1, y1 = path[i].split(",")[::-1]
        x1, y1 = int(x1), int(y1)
        x2, y2 = path[i + 1].split(",")[::-1]
        x2, y2 = int(x2), int(y2)

        rock_lines = construct_rock_lines(x1,y1,x2,y2)
        for (x,y) in rock_lines:
            map[x, y] = ROCK
            max_depth = max(x, max_depth)

print(map)
part_1_map = map.copy()
print(max_depth)
part_1_counter = 0
full_sand_flag = False
while not full_sand_flag:
    row, column = 0, 500
    part_1_counter += 1
    while True:
        if row > max_depth:
            part_1_counter -= 1
            full_sand_flag = True
            break
        elif part_1_map[row+1, column] == AIR:
            row += 1
        elif part_1_map[row+1, column-1] == AIR:
            row += 1
            column -= 1
        elif part_1_map[row+1, column+1] == AIR:
            row += 1
            column += 1
        else:
            part_1_map[row, column] = SAND
            break

print(part_1_counter)


"""PART 2"""
max_depth = max_depth + 2
part_2_map = map.copy()
part_2_counter = 0
full_sand_flag = False
while not full_sand_flag:
    row, column = 0, 500
    part_2_counter += 1
    while True:
        if row + 1 >= max_depth:
            part_2_map[row, column] = SAND
            break
        elif part_2_map[1, 499] == SAND \
                and part_2_map[1, 500] == SAND \
                and part_2_map[1, 501] == SAND:
            full_sand_flag = True
            break
        elif part_2_map[row+1, column] == AIR:
            row += 1
        elif part_2_map[row+1, column-1] == AIR:
            row += 1
            column -= 1
        elif part_2_map[row+1, column+1] == AIR:
            row += 1
            column += 1
        else:
            part_2_map[row, column] = SAND
            break

print(part_2_counter)
