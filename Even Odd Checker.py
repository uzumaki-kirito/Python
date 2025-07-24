def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number: "))
result = even_or_odd(number)
print(f"The number is {result}.")