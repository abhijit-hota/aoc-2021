from functools import reduce
from pprint import pprint

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
illegal_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
autocomplete_points = {")": 1, "]": 2, "}": 3, ">": 4}


# Returns (bool, val)
# if chunk is illegal, bool is True and val is the illegal char
# if chunk is incomplete, bool is False and val is the required completions
def get_illegal_incomplete(chunk):
    stack = []

    for char in chunk:
        if char not in pairs:  # If it's a closing char
            if pairs[stack[len(stack) - 1]] == char:
                stack.pop()
            else:
                return True, char
        else:
            stack.append(char)

    return False, reversed([pairs[char] for char in stack])


def get_illegal_score(program):
    score = 0
    for chunk in program:
        illegal, char = get_illegal_incomplete(chunk)
        if illegal:
            score += illegal_points[char]

    return score


def get_autocomplete_score(chunks):
    completions = [get_illegal_incomplete(x) for x in chunks]
    scores = [
        reduce(lambda prev, curr: 5 * prev + autocomplete_points[curr], completion, 0)
        for incomplete, completion in completions
        if not incomplete
    ]

    return sorted(scores)[len(scores) // 2]


with open("../inputs/10_syntax_scoring.txt", "r") as f:
    program = [x.strip() for x in f.readlines()]

    solution_one = get_illegal_score(program)
    print(solution_one)

    solution_two = get_autocomplete_score(program)
    print(solution_two)
