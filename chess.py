def on_same_row_or_column(start, end):

    return start[0] == end[0] or start[1] == end[1]


def is_move_possible(figure, start, end):

    dx = abs(ord(start[0]) - ord(end[0]))
    dy = abs(int(start[1]) - int(end[1]))

    if start == end:
        return 'False'

    if figure == 'пешка':

        if start[0] == end[0]:
            return int(end[1]) - int(start[1]) == 1

    elif figure == 'ладья':
        return on_same_row_or_column(start, end)

    elif figure == 'королева':
        return on_same_row_or_column(start, end) or dx == dy

    elif figure == 'слон':
        return dx == dy

    elif figure == 'король':
        return dx <= 1 and dy <= 1

    elif figure == 'конь':
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


positions = [i for i in input().split('-')]
piece = input()

pos_start = positions[0]
pos_end = positions[1]

print(is_move_possible(piece, pos_start, pos_end))
