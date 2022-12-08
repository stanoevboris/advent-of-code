actions_1 = {'A': 1, 'B': 2, 'C': 3}
actions_2 = {'X': 1, 'Y': 2, 'Z': 3}
win = 6
draw = 3
lose = 0


def game(player_1, player_2):
    if player_1 == player_2:
        return draw + player_2
    elif player_1 == 1 and player_2 == 3:
        return lose + player_2
    elif player_1 == 2 and player_2 == 1:
        return lose + player_2
    elif player_1 == 3 and player_2 == 2:
        return lose + player_2
    elif player_2 == 1 and player_1 == 3:
        return win + player_2
    elif player_2 == 2 and player_1 == 1:
        return win + player_2
    elif player_2 == 3 and player_1 == 2:
        return win + player_2


def game_2(p1_action, p2_action):
    if p2_action == 'X':
        if p1_action == 'A':
            return lose + actions_2.get('Z')
        elif p1_action == 'B':
            return lose + actions_2.get('X')
        else:
            return lose + actions_2.get('Y')
    elif p2_action == 'Y':
        if p1_action == 'A':
            return draw + actions_2.get('X')
        elif p1_action == 'B':
            return draw + actions_2.get('Y')
        else:
            return draw + actions_2.get('Z')
    else:
        if p1_action == 'A':
            return win + actions_2.get('Y')
        elif p1_action == 'B':
            return win + actions_2.get('Z')
        else:
            return win + actions_2.get('X')


with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

actions = [line.split() for line in lines]

part_1_score = sum([game(actions_1.get(p1), actions_2.get(p2)) for p1, p2 in actions])
print(part_1_score)

part_2_score = sum([game_2(p1, p2) for p1, p2 in actions])
print(part_2_score)
