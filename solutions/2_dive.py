with open("../inputs/2_dive.txt", "r") as f:

    # Sweet list comprehensions!
    commands = [
        [direction, int(step)] for direction, step in (line.split() for line in f)
    ]

    # Part 1
    horizontal_pos = 0
    depth = 0

    for direction, step in commands:
        if direction == "forward":
            horizontal_pos += step
        elif direction == "down":
            depth += step
        elif direction == "up":
            depth -= step

    print(horizontal_pos * depth)

    # Part 2
    aim = 0
    horizontal_pos = 0
    depth = 0

    for direction, step in commands:
        if direction == "forward":
            horizontal_pos += step
            depth += aim * step
        elif direction == "down":
            aim += step
        elif direction == "up":
            aim -= step

    print(horizontal_pos * depth)
