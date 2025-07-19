Students = []
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter the student name: ")
    grade = int(input("Enter the student grade: "))
    Students.append({"Name": name, "Grade": grade})
for student in Students:
    if student["Grade"] > 80:
        print(student["Name"])