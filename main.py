from iterative_executor import *
from recursive_executor import *

recursive_exec = RecursiveExecutor()
iterative_exec = IterativeExecutor()
print("Task 1")
recursive_exec.print_decimal_division(3789)
print()
iterative_exec.print_decimal_division(3789)
print()
print("Task 2")
print(recursive_exec.calculate_crazy_roots(6, 2))
