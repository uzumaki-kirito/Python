students = [
    {"Name": "Hasan", "Grade": 82},
    {"Name": "Anika", "Grade": 85},
    {"Name": "Pritom", "Grade": 79}
]

for student in students:
    if student["Grade"] > 80:
        print(student["Name"])
