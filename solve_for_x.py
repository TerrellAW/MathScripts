import re

def is_valid_math_expression(x):
    # Define the regex pattern
    pattern = re.compile(r'^\s*[+-]?\s*(\d+(\.\d*)?|\.\d+|\dx|\dx\.\d*)\s*([+\-*/^]\s*(\d+(\.\d*)?|\.\d+|\dx|\dx\.\d*)\s*)*\s*=\s*(\d+(\.\d*)?|\.\d+|\dx|\dx\.\d*)\s*$')

    # Check if valid
    return bool(pattern.match(s))

def solve_for_x(x):
    # Initialize variables
    value = 0

    # Ensure input is a valid string
    x_string = str(x)
    isValid = is_valid_math_expression(x_string)

    if isValid:
        # Parse string to find numbers and position of x
        parts = x_string.split('=') # Split equation with '='
        if len(parts) == 2: # Ensure its a valid equation
            value = parts[1].strip() # Take second part and strip white spaces
        else:
            print("Invalid equation.")
            return
    else:
        print("Invalid equation.")
        return

# Handle input and output for terminal
def main():
