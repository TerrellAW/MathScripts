import re

def is_valid_math_expression(x):
    # Define the regex pattern
    pattern = re.compile(r'''
        ^\s*                           # Start, optional whitespace
        [+-]?\s*                       # Optional leading sign
        (\d+(\.\d+)?|                  # Integer or decimal number
        \.\d+|                        # Decimal starting with dot (.5)
        \d*x|                         # Variable with optional coefficient (x, 3x, 12x)
        x)                            # Just x by itself
        \s*
        ([+\-*/]\s*(\d+(\.\d+)?|\.\d+|\d*x|x)\s*)*  # Additional terms
        \s*=\s*                        # Equals sign
        (\d+(\.\d+)?|\.\d+|\d*x|x)     # Right side
        \s*$                           # End
    ''', re.VERBOSE)
    # Check if valid
    return bool(pattern.match(x))

def handle_division(expression: str, value: float):
    if '/' in expression:
        div_numbers = re.findall(r'\/(\d+(?:\.\d+)?|\.\d+)', expression)
        for num_str in div_numbers:
            value *= float(num_str)
    return value

def handle_multiplication(expression: str, value: float):
    if '*' in expression or re.search(r'\d*\.?\d*x', expression):
        # Explicit multiplication
        ex_mult_numbers = re.findall(r'\*(\d+(?:\.\d+)?|\.\d+)', expression)
        #Implicit multiplication
        imp_mult_numbers = re.findall(r'(\d+(?:\.\d+)?|\.\d+)x', expression)

        mult_numbers = ex_mult_numbers + imp_mult_numbers

        for num_str in mult_numbers:
            num = float(num_str)
            if num != 0:
                value /= num
    return value

def handle_add_subtract(expression: str, value: float):
    if '+' in expression:
        add_numbers = re.findall(r'\+(\d+(?:\.\d+)?|\.\d+)', expression)
        for num_str in add_numbers:
            value -= float(num_str)
    if '-' in expression:
        sub_numbers = re.findall(r'\-(\d+(?:\.\d+)?|\.\d+)', expression)
        for num_str in sub_numbers:
            value += float(num_str)
    return value

def simplify(expression: str):
    # Handle negative numbers

    # Handle parentheses

    return expression

def solve_for_x(equation):
    # Initialize variables
    value = float(equation.split('=')[1].strip())
    expression = equation.split('=')[0].strip()

    # Handle parentheses and negative numbers
    expression = simplify(expression)

    # Handle addition and subtraction
    value = handle_add_subtract(expression, value)

    # Handle division
    value = handle_division(expression, value)

    # Handle multiplication
    value = handle_multiplication(expression, value)

    print(f"x = {value}")

# Handle input and output for terminal
def main():
    print("Solve for X")

    # Take user input
    validated = False
    equation = ""
    while not validated:
        equation = input("Enter an equation: ")

        # Validate user input
        if not is_valid_math_expression(equation):
            print("Invalid equation.")
            continue
        else:
            validated = True

    # Solve for x
    solve_for_x(equation)

main()

# TODO: Refactor to implement this approach instead
# 1. Parse into terms: "2x + 3x - 5 = 10"
#    becomes: [Term("2x"), Term("+3x"), Term("-5")]

# 2. Separate variable and constant terms:
#    variable_terms = ["2x", "+3x"]
#    constant_terms = ["-5"]

# 3. Combine like terms:
#    total_coefficient = 2 + 3 = 5
#    total_constants = -5

# 4. Move constants to other side:
#    5x = 10 + 5 = 15

# 5. Solve: x = 15/5 = 3
