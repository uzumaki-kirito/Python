Students = []
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter the student name: ")
    grade = int(input("Enter the student grade: "))
    Students.append({"Name": name, "Grade": grade})
highest = Students[0]
for student in Students:
    if student["Grade"] > highest["Grade"]:
        highest = student
print(f"Top student: {highest['Name']}")