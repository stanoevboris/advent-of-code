def convert_char_to_number(character: str):
    return ord(character) - 96


def valid_coordinates(maze: list, x: int, y: int) -> bool:
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
        return True
    else:
        return False


map = []
with open('input.txt', 'r') as file:
    lines = file.read().split("\n")

for line in lines:
    map.append(line)

queue = []
visited = set()

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 'S' or map[i][j] == 'a':
            queue.append(((i, j), 0))
            visited.add((i, j))
            map[i] = map[i].replace("S", 'a')

actions = {"up": [1, 0], "down": [-1, 0], "right": [0, 1], "left": [0, -1]}

while True:

    (x, y), distance = queue.pop(0)

    if map[x][y] == 'E':
        queue.append(((x, y), distance))
        break

    distance += 1
    for action in actions:
        direction = actions[action]
        new_x = direction[0] + x
        new_y = direction[1] + y

        if valid_coordinates(map, new_x, new_y) and (new_x, new_y) not in visited:
            if convert_char_to_number(map[new_x][new_y]) - convert_char_to_number(map[x][y]) <= 1:
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y), distance))

print(queue[-1][-1])
