def get_user_number() -> float:
    """
    Ask the user for a number and keeps asking until a valid number is entered.
    :return:
    float: A valid numeric value entered by the user.
    """
    while True:
        user_input = input("Enter a number: ")
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation() -> str:
    """
    Ask the user for an operation symbol and keeps asking until a valid operation is entered.
    :return: 
    str: One of '+', '-', '*', or '/'
    """
    valid_operations = ["+", "-", "*", "/"]
    while True:
        operation = input("Enter an operation (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        else:
            print("Invalid input. Please enter +, -, *, or /.")