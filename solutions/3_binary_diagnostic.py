from collections import Counter


with open("../inputs/3_binary_diagnostic.txt", "r") as f:
    report = [line.rstrip() for line in f]
    # "width" of each input/diagnostic
    width = len(report[0])

    """
    Part 1
    The solution is O(N*W) where N = number of inputs and W = length of each input
    A better solution is probably possible using bit manipulation
    """

    # We make a 2 * width matrix
    # 0th index stores the 0 counts of the ith place
    # 1st index stores the 1 counts of the ith place
    oxygen_count = [[0, 0] for _ in range(width)]

    for bits in report:
        for i in range(width):
            oxygen_count[i][int(bits[i])] += 1

    # Finding the most occuring bit
    gamma = "".join([("0" if zeros > ones else "1") for [zeros, ones] in oxygen_count])

    # Finding the least occuring bit: the opposite of the previous
    epsilon = "".join([("1" if bit == "0" else "0") for bit in gamma])

    # Converting binary to decimal by passing 2 as the radix
    solution = int(gamma, 2) * int(epsilon, 2)

    print(solution)

    """
    Part 2
    We can't use the previous mostly_occuring array to find the oxygen generator rating and CO2 scrub rating
    """

    # Making copies of arrays
    # Not at all space efficient
    
    oxygen_rating = list(report)
    co2_rating = list(report)

    for i in range(width):

        if len(oxygen_rating) > 1:
            oxygen_count = Counter([f[i] for f in oxygen_rating])
            most_common = "0" if (oxygen_count["0"] > oxygen_count["1"]) else "1"
            oxygen_rating = [*filter(lambda x: x[i] == most_common, oxygen_rating)]

        if len(co2_rating) > 1:
            co2_count = Counter([f[i] for f in co2_rating])
            least_common = "0" if (co2_count["0"] <= co2_count["1"]) else "1"
            co2_rating = [*filter(lambda x: x[i] == least_common, co2_rating)]

    second_solution = int(oxygen_rating[0], 2) * int(co2_rating[0], 2)
    print(second_solution)
