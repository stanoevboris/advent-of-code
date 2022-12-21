import json
from functools import cmp_to_key
from math import prod


def compare_integers(a: int, b: int):
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1


def compare(a, b):
    for element_a, element_b in zip(a, b):
        comp = 0
        if isinstance(element_a, int) and isinstance(element_b, int):
            comp = compare_integers(element_a, element_b)
        else:
            if isinstance(element_a, int):
                element_a = [element_a]
            if isinstance(element_b, int):
                element_b = [element_b]
            comp = compare(element_a, element_b)

        if comp != 0:
            return comp

    if len(a) == len(b):
        return 0
    elif len(a) < len(b):
        return -1
    else:
        return 1


"""======PART 1======"""
with open('input.txt', 'r') as file:
    lines = file.read().split('\n\n')
counter = 0
for idx, line in enumerate(lines):
    list_one, list_two = line.split("\n")
    list_one = json.loads(list_one)
    list_two = json.loads(list_two)

    if compare(list_one, list_two) <= 0:
        counter += idx + 1

print(counter)
"""======PART 1 FINISHED======="""

"""======PART 2========"""
with open("input.txt", 'r') as file:
    lines = file.read().split("\n")

print(lines)
packets = [json.loads(line) for line in lines if len(line.strip())]
packets.append([[2]])
packets.append([[6]])

sorted_packets = sorted(packets, key=cmp_to_key(compare))
print(sorted_packets)

part_2_score = prod([idx + 1 for idx, packet in enumerate(sorted_packets) if packet == [[2]] or packet == [[6]]])
print(part_2_score)
