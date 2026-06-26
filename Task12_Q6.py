square = lambda x: x ** 2
try:
    numbers = range(1, 21)
    squares = [square(num) for num in numbers]

    # Display all squares
    print("Squares of numbers from 1 to 20:")
    print(squares)

    # Print only even squares
    print("\nEven Squares:")
    for num in squares:
        if num % 2 == 0:
            print(num, end =" ")
except Exception as e:
    print("Error : ", e)