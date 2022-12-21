import re
from tqdm import tqdm
import math

with open('input.txt', 'r') as file:
    lines = file.read().split('\n\n')

monkey_items = {}
monkey_transfers = {}

monkey_data = lines[0].split('\n')
current_monkey = 0
for line in lines:
    monkey_data = line.split('\n')
    for data in monkey_data:
        if 'Monkey' in data:
            monkey_items[current_monkey] = {}
            monkey_transfers[current_monkey] = 0
            continue
        elif 'Starting items' in data:
            starting_items = [int(x) for x in re.findall(r"\d+", data)]
            monkey_items[current_monkey]['starting_items'] = starting_items
        elif 'Operation' in data:
            operation = data.split("=")[1].strip()
            monkey_items[current_monkey]['operation'] = operation
        elif 'Test' in data:
            test_number = [int(x) for x in re.findall(r"\d+", data)][0]
            monkey_items[current_monkey]['divisible'] = test_number
        elif 'true' in data:
            true_case = [int(x) for x in re.findall(r"\d+", data)][0]
            monkey_items[current_monkey]['true_case'] = true_case
        elif 'false' in data:
            false_case = [int(x) for x in re.findall(r"\d+", data)][0]
            monkey_items[current_monkey]['false_case'] = false_case

    current_monkey += 1

print(monkey_items)

rounds = 10000
mod = math.prod(monkey_items[monkey]['divisible'] for monkey in monkey_items)

for round in tqdm(range(rounds)):
    for monkey in monkey_items.keys():
        current_monkey_items = monkey_items[monkey]['starting_items'].copy()
        for idx, item in enumerate(current_monkey_items):
            monkey_transfers[monkey] += 1
            operation = monkey_items[monkey]['operation'].replace("old", "item")
            # new_worry_level = int(eval(operation) / 3)
            new_worry_level = int(eval(operation) % mod)
            divisible_value = monkey_items[monkey]['divisible']
            if new_worry_level % divisible_value == 0:
                true_case_monkey = monkey_items[monkey]['true_case']
                monkey_items[true_case_monkey]['starting_items'].append(new_worry_level)
                monkey_items[monkey]['starting_items'].remove(item)
            else:
                false_case_monkey = monkey_items[monkey]['false_case']
                monkey_items[false_case_monkey]['starting_items'].append(new_worry_level)
                monkey_items[monkey]['starting_items'].remove(item)

print(monkey_transfers)

max_values = sorted(monkey_transfers, key=monkey_transfers.get, reverse=True)[:2]
part_one_score = 1

for value in max_values:
    score = monkey_transfers[value]
    part_one_score *= score

print(part_one_score)
