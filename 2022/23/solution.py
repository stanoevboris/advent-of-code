import numpy as np
from tqdm import tqdm
moves = {
    'N': {'value': [-1, 0],
          'NE': [-1, 1],
          'NW': [-1, -1]},

    'S': {'value': [1, 0],
          'SE': [1, 1],
          'SW': [1, -1]},

    'W': {'value': [0, -1],
          'NW': [-1, -1],
          'SW': [1, -1]},
    'E': {'value': [0, 1],
          'NE': [-1, 1],
          'SE': [1, 1]}
}

# moving_rules = ['N', 'NE', 'NW',
#                 'S', 'SE', 'SW',
#                 'W', 'NW', 'SW',
#                 'E', 'NE', 'SE']

moving_rules = ['N', 'S', 'W', 'E']


# def is_withing_map(x, y):
#     if 0 <= x < len(grove) and 0 <= y < len(grove[0]):
#         return True
#     return False


def propose_move(elf_idx, x, y, current_elfs, new_elfs):
    move_flag = True
    for rule in moving_rules:
        directions = moves[rule]

        for direction in directions:
            new_coordinates = [a + b for a, b in zip([x, y], moves[rule][direction])]
            if new_coordinates in current_elfs.values():
                move_flag = False

    if move_flag:
        return current_elfs[elf_idx]


    for rule in moving_rules:
        directions = moves[rule]
        move_flag = True
        for direction in directions:
            new_coordinates = [a + b for a, b in zip([x, y], moves[rule][direction])]
            if new_coordinates in current_elfs.values():
                move_flag = False

        if move_flag:
            new_elfs[elf_idx] = [a + b for a, b in zip([x, y], moves[rule]['value'])]
            return new_elfs[elf_idx]

    return current_elfs[elf_idx]



def second_round_check(elf_idx, x, y, new_elfs, current_elfs):
    for elf in new_elfs.keys():
        if elf == elf_idx:
            continue
        else:
            if new_elfs[elf] == new_elfs[elf_idx]:
                new_elfs[elf] = current_elfs[elf]
                new_elfs[elf_idx] = current_elfs[elf_idx]

    return new_elfs


def iterate_round(current_elfs, elfs_moved=0):
    new_elfs = current_elfs.copy()
    for elf in current_elfs:
        x, y = current_elfs[elf]
        new_elfs[elf] = propose_move(elf, x, y, current_elfs=current_elfs, new_elfs=new_elfs)

    for elf in current_elfs:
        x, y = current_elfs[elf]
        new_elfs = second_round_check(elf, x, y,
                                      new_elfs=new_elfs,
                                      current_elfs=current_elfs)

    elfs_next_current_position = new_elfs.copy()

    for elf in elfs_next_current_position:
        if elfs_next_current_position[elf] != current_elfs[elf]:
            elfs_moved += 1

    return elfs_next_current_position, elfs_moved


with open('input', 'r') as file:
    lines = file.read().split("\n")

grove = []

for line in lines:
    grove.append(list(line))

grove = np.array(grove)
print("INITIAL GROVE")
print(np.matrix(grove))
print("=========")
indexes = np.where(grove == '#')
elfs_position = list(zip(indexes[0], indexes[1]))
elfs_position = [list(el) for el in elfs_position]
elfs_current_position = {idx: elfs_position[idx] for idx in range(len(elfs_position))}
elfs_new_positions = elfs_current_position.copy()

for round in tqdm(range(10)):
    elfs_current_position, var = iterate_round(elfs_current_position, 0)
    moving_rules.append(moving_rules.pop(0))


print(elfs_current_position)

x_min = min([coordinate[0] for coordinate in elfs_current_position.values()])
x_max = max([coordinate[0] for coordinate in elfs_current_position.values()])
y_min = min([coordinate[1] for coordinate in elfs_current_position.values()])
y_max = max([coordinate[1] for coordinate in elfs_current_position.values()])
# print(y_max - y_min)
print(x_max)
print(x_min)
print(y_min)
print(y_max)

# print(area)
part_1_score = (abs(x_max - x_min) + 1) * (abs(y_max - y_min) + 1) - len(elfs_current_position.keys())

print(part_1_score)
round = 0
elfs_current_position = {idx: elfs_position[idx] for idx in range(len(elfs_position))}
moving_rules = ['N', 'S', 'W', 'E']

while True:

    elfs_moved = 0

    elfs_current_position, elfs_moved = iterate_round(elfs_current_position, elfs_moved)
    moving_rules.append(moving_rules.pop(0))

    if elfs_moved == 0:
        print(f"Round {round+1}")
        break
    round += 1
