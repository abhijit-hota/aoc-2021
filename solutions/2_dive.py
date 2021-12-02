with open("../inputs/2_dive.txt", "r") as f:
    # commands = list(map(lambda command: command.split(), f.read().splitlines()))

    # Making a commands array of arrays
    # Wanted to use list comprehension but couldn't find a way.
    # This is readable and sweet.
    commands = []
    for line in f:
        [direction, step] = line.split()
        commands.append([direction, int(step)])

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