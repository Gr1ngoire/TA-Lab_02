# Variant 3
import math


def calculate_crazy_roots(start, diff, depth, init_start):
    if (not int(start)) or (not int(depth)) or (diff >= start):
        return "Depth ans start params must be integer and diff must be less than start"

    print("adder", start)
    print("mnogitel", start - diff)
    return (start - diff) * math.sqrt(
        start + (0 if start - depth == init_start - 1 else calculate_crazy_roots(start + 1, diff, depth, init_start)))

    # if start - depth != init_start:
    #     print("Mnogitel", start, start - diff)
    #     return (start - diff) * math.sqrt(start + calculate_crazy_roots(start + 1, diff, depth, init_start))
    # else:
    #     print("final", start)
    #     return 0

def crazy_roots_calculator_wrapper(number, depth):
    return calculate_crazy_roots(number, number - 1, depth, number)