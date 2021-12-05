def update_intersections(board, x1, x2, y1, y2):
    x_err = -1 if x1 > x2 else 1
    y_err = -1 if y1 > y2 else 1

    x_range = (
        ([x1] * (abs(y2 - y1) + 1)) if (x1 == x2) else range(x1, x2 + x_err, x_err)
    )
    y_range = (
        ([y1] * (abs(x2 - x1) + 1)) if (y1 == y2) else range(y1, y2 + y_err, y_err)
    )

    for i, j in zip(x_range, y_range):
        board[i][j] += 1
    return board


def count_intersections(board):
    num_intersections = 0
    for row in board:
        for elem in row:
            if elem >= 2:
                num_intersections += 1
    return num_intersections


def make_intersections_board(lines, part=2):
    n = 1000
    board = [[0] * n for _ in range(n)]
    for [x1, y1], [x2, y2] in lines:
        if part == 2 or x1 == x2 or y1 == y2:
            board = update_intersections(board, x1, x2, y1, y2)
    return board


with open("../inputs/5_hydrothermal_venture.txt", "r") as f:
    lines = [
        [[int(x) for x in a.split(",")] for a in line.strip().split(" -> ")]
        for line in f
    ]

    intersections = make_intersections_board(lines)
    num_intersections = count_intersections(intersections)

    print(num_intersections)
