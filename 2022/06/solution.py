from collections import Counter


def is_unique_chars(substring):
    # Counting frequency
    freq = Counter(substring)
    if len(freq) == len(substring):
        return True
    else:
        return False


with open('input.txt', 'r') as file:
    line = file.read().split('\n')

print(line)
string = line[0]

part_1_result = -1
for idx in range(len(string) - 4):
    substring = string[idx: idx + 4]
    if is_unique_chars(substring):
        part_1_result = idx + 4
        break
print(part_1_result)


part_2_result = -1
for idx in range(len(string) - 14):
    substring = string[idx: idx + 14]
    if is_unique_chars(substring):
        part_2_result = idx + 14
        break
print(part_2_result)
