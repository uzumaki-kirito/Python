try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero.")
except ValueError:
    print("❌ Error: Please enter valid numbers.")
