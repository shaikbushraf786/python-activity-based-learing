students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter student name: ")

    m1 = int(input("Enter Maths marks: "))
    m2 = int(input("Enter Physics marks: "))
    m3 = int(input("Enter Chemistry marks: "))

    attendance = float(input("Enter attendance percentage: "))
    income = int(input("Enter annual family income: "))

    total = m1 + m2 + m3
    aggregate = total / 3

    if (aggregate >= 75 and
        m1 >= 50 and m2 >= 50 and m3 >= 50 and
        attendance >= 75 and income <= 200000):

        students.append([
            name, aggregate, attendance, income
        ])

    else:
        print(name, "is Not Eligible")

# Sort students based on criteria
students.sort(key=lambda x: (
    -x[1], -x[2], x[3]
))

print("\n--- Scholarship Eligible Students ---")

if len(students) == 0:
    print("No students are eligible.")

else:
    print("Rank\tName\tAggregate\tAttendance\tIncome")

    for rank, student in enumerate(students, start=1):
        print(rank, "\t", student[0], "\t",
              round(student[1], 2), "\t\t",
              student[2], "\t\t", student[3])

