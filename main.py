# Modern Calculator in Python

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Function to display the calculator menu
def display_menu():
    print("Welcome to Modern Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

# Function to get user input for numbers and operation choice
def get_user_input():
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid input. Please enter a valid option.")
        return get_user_input()
    elif choice == '5':
        return None, None, 'exit'
    else:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2, choice
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return get_user_input()

# Function to perform calculation based on user choice
def perform_operation(num1, num2, choice):
    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    elif choice == '4':
        try:
            result = divide(num1, num2)
            operation = '/'
        except ValueError as e:
            print(e)
            return None, None
    else:
        return None, None

    print(f"{num1} {operation} {num2} = {result}")
    return result, operation

# Main function to run the calculator
def main():
    while True:
        display_menu()
        num1, num2, choice = get_user_input()
        if choice == 'exit':
            print("Exiting Modern Calculator. Goodbye!")
            break
        result, _ = perform_operation(num1, num2, choice)
        if result is not None:
            print(f"Result: {result}")
        print()

# Run the calculator
if __name__ == "__main__":
    main()
