def add (a,b):
    return a+b
x,y = map(int, input("Enter Two Numbers: ").split())
Sum = add(x,y)
print(f"Total = {Sum}")