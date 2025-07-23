n = int(input("Enter how many numbers: "))
largest = 0
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    if num > largest:
        largest = num
print("largest Number is:", largest)
    