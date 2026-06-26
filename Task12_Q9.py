import math
import random
from datetime import datetime
history = {}

# Function for Basic Arithmetic
def basic_arithmetic():
    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter Choice: "))
        if choice == 1:
            result = num1 + num2
            operation = f"{num1} + {num2}"

        elif choice == 2:
            result = num1 - num2
            operation = f"{num1} - {num2}"

        elif choice == 3:
            result = num1 * num2
            operation = f"{num1} * {num2}"

        elif choice == 4:
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
            operation = f"{num1} / {num2}"

        else:
            print("Invalid Choice!")
            return

        print("Result =", result)
        return operation, result

    except ValueError:
        print("Error: Enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    return None

# Function for Scientific Calculations
def scientific_calculation():
    try:
        print("\n1. Square Root")
        print("2. Power")
        print("3. Factorial")
        choice = int(input("Enter Choice: "))
        if choice == 1:
            num = float(input("Enter Number: "))
            result = math.sqrt(num)
            operation = f"sqrt({num})"

        elif choice == 2:
            base = float(input("Enter Base: "))
            power = float(input("Enter Power: "))
            result = math.pow(base, power)
            operation = f"{base}^{power}"

        elif choice == 3:
            num = int(input("Enter Number: "))
            result = math.factorial(num)
            operation = f"{num}!"

        else:
            print("Invalid Choice!")
            return

        print("Result =", result)
        return operation, result

    except ValueError:
        print("Error: Invalid Input.")
    except Exception as e:
        print("Error:", e)
    return None

# Function to Generate Random Number
def random_number():
    try:
        start = int(input("Enter Start Number: "))
        end = int(input("Enter End Number: "))

        result = random.randint(start, end)
        operation = f"Random Number ({start}-{end})"

        print("Generated Number =", result)
        return operation, result

    except ValueError:
        print("Error: Enter valid integers.")
    return None

# Main Menu
while True:
    print("\n****** SMART CALCULATOR & DATA MANAGER ******")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Number")
    print("4. View History")
    print("5. Exit")

    try:
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            data = basic_arithmetic()

        elif choice == 2:
            data = scientific_calculation()

        elif choice == 3:
            data = random_number()

        elif choice == 4:
            if history:
                print("\n******* Calculation History ******")
                for time, details in history.items():
                    print(time, "->", details)
            else:
                print("No History Available.")
            continue

        elif choice == 5:
            print("Thank You! Program Ended.")
            break

        else:
            print("Invalid Choice!")
            continue

        # Store result with timestamp
        if data:
            operation, result = data
            timestamp = str(datetime.now())
            history[timestamp] = f"{operation} = {result}"
    except ValueError:
        print("Error: Please enter a valid menu choice.")