# exceptions_example.py

user_input = input("Enter a number: ")

try:
    number = int(user_input)
    print(f"The number is {number}.")

    result = 10 / number
    print(f"Result is: {result}")

except ValueError:
    print("Error: Input is not a valid number. Please enter an integer.")

except ZeroDivisionError:
    print("Error: Division by zero is undefined!")
