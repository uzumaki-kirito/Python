colors = tuple(input("Enter items separated by space: ").split())
search = input("Enter the item to search: ")
if search in colors:
    index = colors.index(search)
    print(f"Index of '{search}': {index}")
else:
    print("Not found")