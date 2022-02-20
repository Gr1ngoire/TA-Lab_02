import math


class RecursiveExecutor:
    def __init__(self):
        pass

    def print_decimal_division(self, number):
        if number < 0 or (not int(number)):
            return "You have entered wrong number, it must be bigger then 0, and integer"

        if 0 <= number <= 9:
            print(number, end="")
        else:
            self.print_decimal_division(number//10)
            print(number % 10, end="")

        # degree - is a parameter you need to add
        # if 0 <= number <= 9:
        #     return number * 10 ** degree
        # else:
        #     print(f"{(number % 10) * 10**degree} + ")
        #     return str(print_decimal_division_recursively(number // 10, degree


    def __calculate_crazy_roots(self, start, diff, depth):
        if (not int(start)) or (not int(depth)) or (diff >= start):
            return "Depth ans start params must be integer and diff must be less than start"

        return (start - diff) * math.sqrt(
            start + (0 if start - depth == diff else self.__calculate_crazy_roots(start + 1, diff, depth)))

        # if start - depth != init_start:
        #     print("Mnogitel", start, start - diff)
        #     return (start - diff) * math.sqrt(start + calculate_crazy_roots(start + 1, diff, depth, init_start))
        # else:
        #     print("final", start)
        #     return 0

    def calculate_crazy_roots(self, number, depth):
        return self.__calculate_crazy_roots(number, number - 1, depth)
