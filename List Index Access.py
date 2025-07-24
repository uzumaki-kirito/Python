my_list = list(map(int, input("Enter the Number for list : ").split()))
try:
    print("List:", my_list)
    index = int(input("Enter an index to access: "))
    value = my_list[index]
    print("Value at index", index, "is:", value)
except ValueError:
    print("❌ Error: Please enter a valid integer index.")
except IndexError:
    print("❌ Error: Index out of range.")
