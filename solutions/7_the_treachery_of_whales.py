def part_one(positions):
    size = len(positions)
    median = sum(sorted(positions)[(size // 2) - 1 : (size // 2) + 1]) // 2

    fuel = sum([abs(n - median) for n in positions])
    return fuel


def part_two(positions):
    max_range = range(max(positions) + 1)

    fuel = min(
        [
            sum([(abs(n - i) * (abs(n - i) + 1)) // 2 for n in positions])
            for i in max_range
        ]
    )
    return fuel


with open("../inputs/7_the_treachery_of_whales.txt", "r") as f:
    positions = [int(x) for x in f.readline().split(",")]

    solution_one = part_one(positions)
    print(solution_one)

    solution_one = part_two(positions)
    print(solution_one)
