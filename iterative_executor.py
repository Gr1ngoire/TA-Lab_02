class IterativeExecutor:
    def __init__(self):
        pass

    def print_decimal_division(self, number):
        new_number = 0
        while number != 0:
            new_number += number % 10
            new_number *= 10
            number //= 10
        new_number //= 10
        while new_number != 0:
            print(new_number % 10, end="")
            new_number //= 10
