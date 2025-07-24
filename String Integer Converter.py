try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print("You entered the number:", number)
except ValueError:
    print("❌ Error: Invalid input! Please enter a valid integer.")
