"""
This was my initial no-brainer implementation which sucked big time
"""


def get_count_brute(initial, days=80):
    output = initial[:]
    for _ in range(days):
        for i, state in enumerate(output):
            if state == 0:
                output[i] = 6
                output.append(8 + 1)
            else:
                output[i] = state - 1

    return len(output)


"""
Using a counter array
I realised you don't actually need hashmaps as all the keys are numbers
"""


def get_count(initial_states, days=80):

    # Making a state counter arrat using list comprehension
    count = [initial_states.count(n) for n in range(9)]

    for _ in range(days):
        # save the number of fish in 0 state
        zeros = count[0]

        # With each day fish in `state` turn to `state + 1`
        for state in range(8):
            count[state] = count[state + 1]
            count[state + 1] = 0

        # And if there are zeros,
        # their state is reset to 6
        count[6] += zeros
        # and that many fish are spawned again
        count[8] += zeros

    return sum(count)


with open("../inputs/6_lanternfish.txt", "r") as f:
    initial_fish = [int(fish) for fish in f.read().split(",")]

    population = get_count(initial_fish, 256)
    print(population)
