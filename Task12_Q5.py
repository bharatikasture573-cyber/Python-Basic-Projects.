import random
import math
try:
    numbers = set()

    # Take 10 numbers as input
    print("Enter 10 numbers:")
    for i in range(10):
        num = int(input(f"Number {i + 1}: "))
        numbers.add(num)
    numbers_tuple = tuple(numbers)
    print("\nUnique Numbers (Tuple):", numbers_tuple)

    if len(numbers_tuple) >= 3:
        random_numbers = random.sample(numbers_tuple, 3)
        print("3 Random Numbers:", random_numbers)
    else:
        print("Less than 3 unique numbers available.")
    total = sum(numbers_tuple)
    print("Sum of Tuple Elements:", total)

    if total >= 0:
        print("Square Root of Sum:", math.sqrt(total))
    else:
        print("Square root cannot be calculated for a negative sum.")
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print("Unexpected Error:", e)