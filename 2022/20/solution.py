class Number:
    def __init__(self, val) -> None:
        self.val = val


def shuffle_list(base_list: list, shuffled_list):
    for element in base_list:
        index = shuffled_list.index(element)

        offset = abs(element.val) % (len(base_list) - 1)
        offset = -offset if element.val < 0 else offset

        new_index = offset + index

        if new_index >= len(base_list):
            new_index = new_index % len(base_list) + 1

        shuffled_list.remove(element)
        shuffled_list.insert(new_index, element)

    return shuffled_list


with open('input.txt', 'r') as file:
    lines = file.read().split("\n")

original_list = []
zero_object = None
for line in lines:
    number = int(line.strip())
    original_list.append(Number(number))
    if number == 0:
        zero_object = original_list[-1]

list_to_shuffle = original_list.copy()
circular_list = shuffle_list(original_list, list_to_shuffle)

part_1_score = 0

zero_index = circular_list.index(zero_object)

for i in [1000, 2000, 3000]:
    index = ((i + zero_index) % len(circular_list))
    part_1_score += circular_list[index].val
print(part_1_score)
"""====PART 1 FINISHED===="""

"""====PART 2===="""
decryption_key = 811589153
decrypted_list = []

for element in original_list:
    decrypted_list.append(Number(decryption_key * element.val))
    if element.val == 0:
        zero_object = decrypted_list[-1]

part_2_circular_list = decrypted_list.copy()

for i in range(10):
    part_2_circular_list = shuffle_list(decrypted_list, part_2_circular_list)

part_2_score = 0
zero_index = part_2_circular_list.index(zero_object)
for i in [1000, 2000, 3000]:
    index = ((i + zero_index) % len(part_2_circular_list))
    part_2_score += part_2_circular_list[index].val

print(part_2_score)
