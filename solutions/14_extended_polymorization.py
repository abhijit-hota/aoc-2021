from collections import Counter

with open("../inputs/14_extended_polymorization.txt", "r") as f:
    atemplate = f.readline().rstrip()
    f.readline()

    rules = dict([x.strip().split(" -> ") for x in f])

    # This is a sweet method of pairing characters I stole from Reddit
    # https://www.reddit.com/r/adventofcode/comments/rfzq6f/comment/hohc8vc
    pair_count = Counter(map(str.__add__, atemplate, atemplate[1:]))

    char_count = Counter(atemplate)

    for _ in range(40):
        for pair, count in pair_count.copy().items():
            replacement = rules[pair]

            prev_pair, next_pair = pair[0] + replacement, replacement + pair[1]

            pair_count[prev_pair] += count
            pair_count[next_pair] += count
            pair_count[pair] -= count

            char_count[replacement] += count

    counts = char_count.values()
    print(max(counts) - min(counts))
