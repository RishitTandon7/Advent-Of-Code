import itertools

def evaluate_expression(numbers, operators):
    """Evaluate the expression from left to right using the numbers and operators."""
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i - 1] == '+':
            result += numbers[i]
        elif operators[i - 1] == '*':
            result *= numbers[i]
    return result

def solve_equations(filename):
    total_calibration_result = 0
    
    # Read the input from the file
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Process each line
    for line in lines:
        test_value_str, numbers_str = line.split(':')
        test_value = int(test_value_str.strip())
        numbers = list(map(int, numbers_str.strip().split()))
        
        # Generate all possible combinations of operators between the numbers
        operator_combinations = itertools.product(['+', '*'], repeat=len(numbers)-1)
        
        for operators in operator_combinations:
            # Evaluate the expression with this combination of operators
            if evaluate_expression(numbers, operators) == test_value:
                total_calibration_result += test_value
                break  # We found a valid expression, no need to check further
        
    return total_calibration_result

# Use the function with the input file
input_file = 'Day7/input.txt'
result = solve_equations(input_file)
print(f"Total calibration result: {result}")
