def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
num = int(input("Enter how many Fibonacci numbers to generate: "))
fib_sequence = fibonacci(num)
print("Fibonacci sequence:", fib_sequence)
