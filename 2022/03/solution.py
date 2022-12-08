def convert_char_to_number(character: str):
    if character.islower():
        return ord(character) - 96
    else:
        return ord(character) - 38


with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

part_1_score = 0
for line in lines:
    first_part, second_part = line[:len(line) // 2], line[len(line) // 2:]
    chars_intersected = list(set(first_part) & set(second_part))
    for char in chars_intersected:
        part_1_score += convert_char_to_number(char)

print(part_1_score)

batch_size = 3
part_2_score = 0
for idx in range(0, len(lines), batch_size):
    print(lines[idx: idx+batch_size])
    chars_intersected = list(set(lines[idx]) & set(lines[idx+batch_size-1]) & set(lines[idx+batch_size-2]))[0]
    part_2_score += convert_char_to_number(chars_intersected)

print(part_2_score)