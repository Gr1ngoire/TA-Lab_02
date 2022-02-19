# Variant 3
import math


def calculate_crazy_roots(start, depth):
    if (not int(start)) or (not int(depth)):
        return "Depth ans start params must be integer"

    return (start - 5) * math.sqrt(start + (0 if start - depth == 5 else calculate_crazy_roots(start + 1, depth)))

    # if start - depth != 6:
    #     print(start, start - 5)
    #     return (start - 5) * math.sqrt(start + calculate_crazy_roots(start + 1, depth))
    # else:
    #     print("final", start)
    #     return start
