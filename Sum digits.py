def sum_of_digits(n):
    return sum(int(digit)
    for digit in str(abs(n)))
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("Sum of digits:", result)