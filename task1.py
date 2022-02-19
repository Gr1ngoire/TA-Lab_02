# Variant 2

def print_deciaml_division_recursively(number, degree):
    if number < 0 or (not int(number)):
        return "You have entered wrong number, it must be bigger then 0, and integer"

    if 0 <= number <= 9:
        return number * 10 ** degree
    else:
        print(f"{(number % 10) * 10**degree} + ")
        return str(print_deciaml_division_recursively(number // 10, degree + 1))
