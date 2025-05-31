#!/bin/bash

# Calculation logic
calculate() {
    local num1=$1
    local num2=$2
    local op=$3

    case "$op" in
        '+') echo $(($num1 + $num2)) ;;
        '-') echo $(($num1 - $num2)) ;;
        '*') echo $(($num1 * $num2)) ;;
        '/') echo $(($num1 / $num2)) ;;
        '%') echo $(($num1 % $num2)) ;;
        '**') echo $(($num1 ** $num2)) ;;
        *) echo "Invalid operator" ;;
    esac
}

# Console Interface
main() {
    echo "========================="
    echo "     BASH CALCULATOR     "
    echo "========================="
    echo "Enter an operator (+, -, *, /, %, **): "
    read operator

    echo "Enter the first number:"
    read num1

    echo "Enter the second number:"
    read num2

    result=$(calculate "$num1" "$num2" "$operator")
    echo "Result: $result"
}

main
