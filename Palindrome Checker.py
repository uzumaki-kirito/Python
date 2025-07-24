def is_palindrome(text):
    return text == text[::-1]
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
