def get_sums(table):
    column_sums = [sum(column) for column in list(map(list, zip(*table)))]
    row_sums = [sum(row) for row in table]

    return (row_sums, column_sums)


def check_bingo(marked_table):
    row_sums, column_sums = get_sums(marked_table)
    return (5 in row_sums) or (5 in column_sums)


def search_number(target, table):
    r = range(len(table))
    for i in r:
        for j in r:
            if table[i][j] == target:
                return (i, j)

    return (None, None)


def get_unmarked_sum(table, marked_table):
    r = range(len(table))
    unmarked_sum = 0

    for i in r:
        for j in r:
            if marked_table[i][j] == 0:
                unmarked_sum += table[i][j]

    return unmarked_sum


def solve_part1(moves, tables):
    marked = [[[0] * 5 for _ in range(5)] for _ in range(len(tables))]

    for move in moves:
        for idx, table in enumerate(tables):
            i, j = search_number(move, table)

            if i == None:
                continue

            marked[idx][i][j] = 1

            if check_bingo(marked[idx]):
                return get_unmarked_sum(table, marked[idx]) * move


def solve_part2(moves, tables):
    marked = [[[0] * 5 for _ in range(5)] for _ in range(len(tables))]
    tables_won = []

    for move in moves:
        for idx, table in enumerate(tables):
            if len(tables_won) == len(tables):
                last_table_idx = tables_won[-1]
                return (
                    get_unmarked_sum(tables[last_table_idx], marked[last_table_idx])
                    * move
                )

            if idx in tables_won:
                continue

            i, j = search_number(move, table)

            if i == None:
                continue

            marked[idx][i][j] = 1

            if check_bingo(marked[idx]):
                tables_won.append(idx)

    return -1


with open("../inputs/4_giant_squid.txt") as f:
    moves = [int(n) for n in f.readline().split(",")]
    f.readline()

    tables = []
    table = []

    for line in f:
        if line == "\n":
            tables.append(table)
            table = []
        else:
            table.append([int(num) for num in line.split()])
    tables.append(table)

    solution_1 = solve_part1(moves, tables)
    print(solution_1)

    solution_2 = solve_part2(moves, tables)
    print(solution_2)
