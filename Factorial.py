def factorial(n):
    result = 1
    if n < 0:
        print("Error")
        return None
    else:
        for i in range(1, n + 1):
            result = result * i
        return result

n = int(input("Enter a Number : "))
result = factorial(n)
if result is not None:
    print(f"Result= {result}")