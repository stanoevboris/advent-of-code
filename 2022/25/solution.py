from math import pow

with open('input', 'r') as file:
    lines = file.read().split("\n")

part_1_sum = 0

for line in lines:
    size = len(line) - 1
    sum = 0
    for idx, char in enumerate(line):
        if char == '-':
            number = -1
        elif char == '=':
            number = -2
        else:
            number = int(char)
        power = pow(5, size - idx)
        sum += int(number * power)

    part_1_sum += sum

print(part_1_sum)

# 4890 = 2=-1=0

# print(4890  5)

mapper = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-", 5: "0"}

base_5 = ""
rest = 0
decimal = part_1_sum
while decimal != 0:
    remainder = decimal % 5 + rest
    rest = 0
    if remainder > 2:
        rest = 1

    base_5 = mapper[remainder] + base_5
    decimal //= 5

print(base_5)
