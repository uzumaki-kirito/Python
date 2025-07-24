try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("❌ Error: Cannot divide by zero.")
            result = None
    else:
        print("❌ Error: Invalid operator.")
        result = None

    if result is not None:
        print(f"Result: {num1} {operator} {num2} = {result}")

except ValueError:
    print("❌ Error: Please enter valid numbers.")
