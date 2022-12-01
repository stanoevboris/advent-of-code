
with open('input.txt', 'r') as file:
    snack_groups = file.read().split('\n\n')

group_values = []
for snack_group in snack_groups:
    parsed_values = [int(val) for val in snack_group.split('\n')]
    current_sum = sum(parsed_values)
    group_values.append(current_sum)

part_1_result = max(group_values)
print(part_1_result)

group_values.sort(reverse=True)
part_2_result = sum(group_values[:3])
print(part_2_result)
