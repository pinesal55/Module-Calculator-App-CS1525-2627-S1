from operations import add, subtract, multiply, divide
from utils import get_user_number, get_operation

print("Welcome to the Calculator!")
number_1 = get_user_number()
number_2 = get_user_number()
operation = get_operation()
if operation == "/" and number_2 == 0:
    print("Can't divide by zero")
    while number_2 == 0:
        print("Please enter a different second number.")
        number_2 = get_user_number()

if operation == '+':
    result = add(number_1, number_2)
elif operation == '-':
    result = subtract(number_1, number_2)
elif operation == '*':
    result = multiply(number_1, number_2)
elif operation == '/':
    result = divide(number_1, number_2)

print(f"{number_1} {operation} {number_2} = {result}")