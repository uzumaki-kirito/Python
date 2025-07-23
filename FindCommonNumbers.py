set1 = set(map(int, input("Enter numbers for Set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter numbers for Set 2 (space-separated): ").split()))

common = set1 & set2  # or: set1.intersection(set2)

print("Common elements:")
for num in common:
    print(num)
