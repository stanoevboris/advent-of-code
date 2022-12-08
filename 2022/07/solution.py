from pathlib import Path

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

print(lines)
pwd = Path("/")
directories = {}

for line in lines:
    command = line.split()
    if command[1] == 'cd':
        new_directory = command[2]
        pwd = pwd / new_directory
        pwd = pwd.resolve()
    elif command[0] != 'dir' and command[1] != 'ls':
        for path in [pwd, *pwd.parents]:
            if path not in directories.keys():
                directories[path] = 0
            directories[path] += int(command[0])

part_1_score = sum([value for value in directories.values() if value < 100000])
print(part_1_score)


sorted_directories = dict(sorted(directories.items(), key=lambda x: x[1], reverse=True))
print(sorted_directories)
current_storage = max(sorted_directories.values())
part_2_score = min([value for value in sorted_directories.values() if value > (30000000-(70000000-current_storage))])

print(part_2_score)
