with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
"""========PART 1==========="""
part_one_score = 0
X_score = 1
cycle_counter = 0
important_cycles = [20, 60, 100, 140, 180, 220]
print(lines)
for line in lines:
    if line == 'noop':
        cycle_counter += 1
        if cycle_counter in important_cycles:
            part_one_score += (cycle_counter * X_score)
        continue
    else:
        action, value = line.split()
        value = int(value)

        for idx in range(2):
            cycle_counter += 1
            if cycle_counter in important_cycles:
                part_one_score += (cycle_counter * X_score)

        X_score += value

print(part_one_score)

"""=======PART 2=========="""
X_score = 1
sprite_pos = 0
important_cycles = [40, 80, 120, 160, 200, 240]
image = []
cycle_counter = 0
current_image = ""
for line in lines:
    if line == 'noop':
        cycle_counter += 1
        if sprite_pos <= cycle_counter <= sprite_pos + 2:
            current_image += "#"
        else:
            current_image += "."

        if cycle_counter in important_cycles:
            image.append(current_image)
            current_image = ""
            cycle_counter = 0
        continue
    else:
        action, value = line.split()
        value = int(value)

        for idx in range(2):
            cycle_counter += 1
            if sprite_pos <= cycle_counter <= sprite_pos + 2:
                current_image += "#"
            else:
                current_image += "."

            if cycle_counter in important_cycles:
                image.append(current_image)
                current_image = ""
                cycle_counter = 0

        X_score += value
        sprite_pos = X_score

for row in image:
    print(row)
