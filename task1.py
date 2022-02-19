# Variant 2

def print_decimal_division_recursively(number):
    if number < 0 or (not int(number)):
        return "You have entered wrong number, it must be bigger then 0, and integer"

    if 0 <= number <= 9:
        print(number, end="")
    else:
        print_decimal_division_recursively(number//10)
        print(number % 10, end="")

    # degree - is a parameter you need to add
    # if 0 <= number <= 9:
    #     return number * 10 ** degree
    # else:
    #     print(f"{(number % 10) * 10**degree} + ")
    #     return str(print_decimal_division_recursively(number // 10, degree + 1))
def print_decimal_division_iteratively(number):
    new_number = 0
    while number != 0:
        new_number += number % 10
        new_number *= 10
        number //= 10
    new_number //= 10
    while new_number != 0:
        print(new_number % 10, end="")
        new_number //= 10