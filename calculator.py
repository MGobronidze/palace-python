import math

def calculator():
    print("Welcome to the Python Calculator!")
    print("You can perform addition (+), subtraction (-), multiplication (*),  division (/), power(^) and _.")
    print("Type 'exit' to end the program.")

    while True:
        # Get user input
        operation = input("\nEnter operation (+, -, *, /, ^, _) or 'exit' to quit: ").strip()
        
        # Exit condition
        if operation.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        # Validate the operation
        if operation not in ['+', '-', '*', '/', '^', '_']:
            print("Invalid operation! Please choose one of +, -, *, /, ^, _.")
            continue
        
        # Get numbers from the user
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
        
        # Perform the calculation
        result = None
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Division by zero is not allowed!")
                continue
            result = num1 / num2
        elif operation == '^':
            result= pow(num1, num2)
        elif operation == '_':
            result = math.sqrt(num1)
        # Display the result
        print(f"The result of {num1} {operation} {num2} is: {result}")

# Start the calculator application
calculator()
