with open('input.txt', 'r') as file:
    actions = file.read().split('\n')

tail = [0, 0]
head = [0, 0]
visited_places = set()

knots = [[0, 0] for x in range(10)]
visited_knots = set()


def move_head(direction_move: str, head_object):
    if direction_move == 'R':
        head_object = [head_object[0], head_object[1] + 1]

    elif direction_move == 'L':
        head_object = [head_object[0], head_object[1] - 1]

    elif direction_move == 'U':
        head_object = [head_object[0] + 1, head_object[1]]

    elif direction_move == 'D':
        head_object = [head_object[0] - 1, head_object[1]]

    return head_object


def move_tail(head_object, tail_object):
    if abs(head_object[0] - tail_object[0]) > 1 or abs(head_object[1] - tail_object[1]) > 1:
        tail_object[0] += (tail_object[0] < head_object[0]) - (head_object[0] < tail_object[0])
        tail_object[1] += (tail_object[1] < head_object[1]) - (head_object[1] < tail_object[1])

    return tail_object


for action in actions:
    direction, steps = action.split()
    steps = int(steps)

    for step in range(steps):
        head = move_head(direction, head)
        tail = move_tail(head, tail)
        visited_places.add(tuple(tail))

        knots[0] = move_head(direction, knots[0])

        for idx in range(len(knots) - 1):
            knots_head = knots[idx]
            knots_tail = knots[idx + 1]

            knots[idx + 1] = move_tail(knots_head, knots_tail)
        visited_knots.add(tuple(knots[-1]))

print(len(visited_places))
print(len(visited_knots))
