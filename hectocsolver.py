import itertools
import random
import sympy

def generate_digits():
    """Generate six random digits (1-9)."""
    return input()

def generate_expressions(digits):
    """Generate all possible expressions with operators and parentheses."""
    operators = ['+', '-', '*', '/', '^', '']
    all_expressions = set()

    # Generate all operator combinations
    for ops in itertools.product(operators, repeat=5):
        expr = "".join(f"{digits[i]}{ops[i]}" for i in range(5)) + str(digits[5])

        # Generate possible parenthesis placements
        bracket_patterns = [
            f"({expr})",  # Full expression in brackets
            f"({digits[0]}{ops[0]}{digits[1]}){ops[1]}({digits[2]}{ops[2]}{digits[3]}){ops[3]}({digits[4]}{ops[4]}{digits[5]})",
            f"(({digits[0]}{ops[0]}{digits[1]}){ops[1]}{digits[2]}){ops[2]}({digits[3]}{ops[3]}{digits[4]}{ops[4]}{digits[5]})"
        ]

        all_expressions.update(bracket_patterns)

    return all_expressions

def find_solution(digits):
    """Find a valid expression that evaluates to 100."""
    expressions = generate_expressions(digits)
    for expr in expressions:
        try:
            if expr.count("^") >1  : continue
            print(expr) 
            if sympy.sympify(expr) == 100:
                return expr
        except:
            continue
    return None

def generate_hectoc_problem():
    """Generate a solvable Hectoc problem."""
    while True:
        digits = generate_digits()
        solution = find_solution(digits)
        if solution:
            return digits, solution

# Generate and print a solvable Hectoc problem
digits, solution = generate_hectoc_problem()
print(f"Hectoc Problem: {digits}")
print(f"Solution: {solution} = 100")
