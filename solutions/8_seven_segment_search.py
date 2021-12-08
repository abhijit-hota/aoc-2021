def part_one(outputs):
    count = 0
    for val in outputs:
        for word in val:
            l = len(word)
            if l in [2, 4, 3, 7]:
                count += 1
    return count


join = lambda arr: "".join(arr)
key = lambda s: join(sorted(s))


def part_two(patterns, outputs):
    input_range = range(len(patterns))
    total_sum = 0

    number_dict = [None, None, "1", "7", "4", None, None, "8"]

    for i in input_range:
        pattern = patterns[i]
        dictionary = {key(s): number_dict[len(s)] for s in pattern}

        # Possible 5, 3, 2s and 0, 6, 9s
        _532 = [*filter(lambda x: len(x) == 5, pattern)]
        _069 = [*filter(lambda x: len(x) == 6, pattern)]

        # Extracting the middle segments from possible 5, 3, 2s
        middle_segments = set(_532[0]) & set(_532[1]) & set(_532[2])

        # We extract the right segment from 1
        one = next(s for s, v in dictionary.items() if v == "1")
        right_segments = set(one)

        # We find the top left segment by taking the difference
        # of the code for 4 middle segments and the right segments
        four = next(s for s, v in dictionary.items() if v == "4")
        top_left_segment = (set(four) - middle_segments - right_segments).pop()

        # Now we start assigning

        # If the entry in _532 has a top left segment, it's a 5
        five = next(code for code in _532 if top_left_segment in code)
        dictionary[key(five)] = "5"

        # If the entry in _532 has a total right segment, it's a 3
        # the < operator in sets is equivalent of isSubset
        three = next(code for code in _532 if right_segments < set(code))
        dictionary[key(three)] = "3"

        # If not five or three, it's a two
        two = next(code for code in _532 if code != five and code != three)
        dictionary[key(two)] = "2"

        # If the entry in _069 has only two middle segments, it's a zero
        zero = next(code for code in _069 if len(middle_segments & set(code)) == 2)
        dictionary[key(zero)] = "0"

        # If the entry in _069 has only one right segment, it's a six
        six = next(code for code in _069 if len(right_segments & set(code)) == 1)
        dictionary[key(six)] = "6"

        # If not six or zero, it's a nine
        nine = next(code for code in _069 if code != six and code != zero)
        dictionary[key(nine)] = "9"

        output = int(join([dictionary[key(num)] for num in outputs[i]]))
        total_sum += output

    return total_sum


with open("../inputs/8_seven_segment_search.txt", "r") as f:
    patterns, outputs = zip(
        *[[x.split() for x in entry.split("|")] for entry in f.readlines()]
    )
    solution_one = part_one(outputs)
    print(solution_one)

    solution_two = part_two(patterns, outputs)
    print(solution_two)
