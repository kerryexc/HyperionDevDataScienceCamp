def perform_calculation():
    while True:
        try:
            num1 = float(input("Enter a number:"))
            num2 = float(input("Enter a second number:"))
            operator = input("Enter an operator (+, -, *, /):")
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero...")
            result = num1 / num2

            with open('equations.txt', 'a+', encoding='utf-8') as file:
                file.write(f"{num1} {operator} {num2} = {round(result, 2)}\n")
                print("\nYour results have been successfully stored.")
            break

        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")


def print_previous_equations():
    try:
        with open('equations.txt', 'r', encoding='utf-8') as file:
            equations = file.readlines()
        if equations:
            print("\nPrevious equations:")
            for equation in equations:
                print(equation.strip())
        else:
            print("\nNo previous equations found.")
    except FileNotFoundError:
        print("No previous equations found.")


def calc_app():
    while True:
        print("\nWelcome to the Calculator App.")
        print("1. Perform Calculation.")
        print("2. Print Previous Equations.")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3):")

        if choice == '1':
            perform_calculation()
        elif choice == '2':
            print_previous_equations()
        elif choice == '3':
            break
        else:
            print("invalid choice. Enter 1, 2, or 3.")

calc_app()