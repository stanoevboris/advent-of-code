with open('input', 'r') as file:
    lines = file.read().split('\n')

print(lines)

pairs = [line.split(',') for line in lines]
part_1_score = 0
part_2_score = 0

for pair in pairs:
    first_pair_start, first_pair_end = pair[0].split('-')
    first_pair_assignments = list(range(int(first_pair_start), int(first_pair_end) + 1))

    second_pair_start, second_pair_end = pair[1].split('-')
    second_pair_assignments = list(range(int(second_pair_start), int(second_pair_end) + 1))

    intersect = list(set(first_pair_assignments) & set(second_pair_assignments))

    # part 1
    if len(intersect) == len(first_pair_assignments) or \
            len(intersect) == len(second_pair_assignments):
        part_1_score += 1

    # part 2
    if len(intersect) != 0:
        part_2_score += 1


print(part_1_score)
print(part_2_score)




