# 1. University Scholarship Allocation – Python Program

## 1. Problem Statement

Design a Python program to allocate university scholarships to students based on the following criteria:

1. Aggregate marks should be 75% or above.
2. Each subject mark should be at least 50.
3. Attendance should be 75% or above.
4. Annual family income should be ₹2,00,000 or below.
5. Eligible students are ranked based on aggregate marks.
6. If two students have the same aggregate marks, attendance is used to resolve the tie.
7. If both aggregate marks and attendance are equal, the student with the lower family income gets the higher rank.

The program displays eligible students along with their ranks.

## 2. Algorithm

1. Start the program.
2. Read the number of students.
3. Enter each student's name.
4. Enter marks in three subjects.
5. Calculate aggregate percentage.
6. Enter attendance percentage.
7. Enter annual family income.
8. Check scholarship eligibility:
   - Aggregate marks ≥ 75%.
   - Each subject mark ≥ 50.
   - Attendance ≥ 75%.
   - Family income ≤ ₹2,00,000.
9. Store eligible students.
10. Sort students based on aggregate marks, attendance, and family income.
11. Assign ranks to eligible students.
12. Display the scholarship eligibility and rank.
13. Stop the program.

## 3. Flowchart

```Mermaid
flowchart TD
    A([Start]) --> B[/Enter number of students/]
    B --> C[/Enter student details/]
    C --> D[Calculate aggregate marks]
    D --> E{Check eligibility criteria}
    E -->|Eligible| F[Add student to eligible list]
    E -->|Not Eligible| G[Reject student]
    F --> H{More students?}
    G --> H
    H -->|Yes| C
    H -->|No| I[Sort eligible students]
    I --> J[Assign ranks]
    J --> K[/Display eligible students and ranks/]
    K --> L([Stop])
```

## 5. Sample Input

```
Enter number of students: 4

Enter details of student 1
Enter student name: Ali
Enter Maths marks: 90
Enter Physics marks: 85
Enter Chemistry marks: 80
Enter attendance percentage: 90
Enter annual family income: 150000

Enter details of student 2
Enter student name: Sana
Enter Maths marks: 80
Enter Physics marks: 75
Enter Chemistry marks: 85
Enter attendance percentage: 85
Enter annual family income: 180000

Enter details of student 3
Enter student name: Ravi
Enter Maths marks: 60
Enter Physics marks: 55
Enter Chemistry marks: 65
Enter attendance percentage: 80
Enter annual family income: 100000

Enter details of student 4
Enter student name: John
Enter Maths marks: 85
Enter Physics marks: 90
Enter Chemistry marks: 80
Enter attendance percentage: 95
Enter annual family income: 120000
```

## 6. Sample Output

```
Ravi is Not Eligible

--- Scholarship Eligible Students ---

Rank    Name    Aggregate    Attendance    Income

1       Ali       85.00         90          150000
2       John      85.00         95          120000
3       Sana      80.00         85          180000
```

Correction to ranking: Since John has 95% attendance and Ali has 90%, John should be Rank 1 and Ali Rank 2.

The correct output is:

```
--- Scholarship Eligible Students ---

Rank    Name    Aggregate    Attendance    Income

1       John      85.00         95          120000
2       Ali       85.00         90          150000
3       Sana      80.00         85          180000
```

