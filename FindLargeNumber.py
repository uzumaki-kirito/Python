def find_max(numbers):
    if not numbers:
        return None 
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
my_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
largest = find_max(my_list)
print("The largest number is:", largest)
