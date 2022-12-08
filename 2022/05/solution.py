from collections import deque
import re
with open('input.txt', 'r') as file:
    crates, actions = file.read().split("\n\n")

print(crates)
stacks = []
for line in crates.splitlines():
    for i, idx in enumerate(range(1, len(line), 4)):
        if i >= len(stacks):
            stacks.append(deque())
        if line[idx] != " ":
            stacks[i].append(line[idx])

for action in actions.splitlines():
    a, b, c= map(int, re.findall(r"\d+", action))
    for value in range(a):
        stacks[c-1].appendleft(stacks[b-1].popleft())

print("".join(last_value[0] for last_value in stacks))
print("PART 1 DONE---------")

stacks = []
for line in crates.splitlines():
    for i, idx in enumerate(range(1, len(line), 4)):
        if i >= len(stacks):
            stacks.append(deque())
        if line[idx] != " ":
            stacks[i].append(line[idx])

for action in actions.splitlines():
    a, b, c= map(int, re.findall(r"\d+", action))
    tmp_list = []
    for value in range(a):
        tmp_list.append(stacks[b-1].popleft())
    while len(tmp_list) > 0:
        stacks[c-1].appendleft(tmp_list.pop())

print("".join(last_value[0] for last_value in stacks))

