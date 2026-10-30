# Hospital Billing and Patient Classification – Python Program

## 1. Problem Statement

Develop a Python program to process hospital billing details by accepting patient information, consultation charges, diagnostic charges, and treatment charges. Calculate the total bill and apply conditional concessions based on patient age and bill amount. Validate billing constraints to ensure that charges and payments are not negative and payment does not exceed the final bill. Finally, classify patients according to their payment status as Fully Paid, Partially Paid, or Pending.

## 2. Algorithm

1. Start the program.
2. Enter patient name and age.
3. Enter consultation charges.
4. Enter diagnostic charges.
5. Enter treatment charges.
6. Enter the amount paid by the patient.
7. Check whether the entered values are valid.
8. Calculate the total bill.
9. Apply 10% concession if patient age is 60 or above.
10. Apply an additional 5% concession if the total bill is above ₹10,000.
11. Calculate the final bill.
12. Validate the payment amount.
13. Classify the payment:
    - Fully Paid – If payment equals the final bill.
    - Partially Paid – If payment is greater than zero but less than the final bill.
    - Pending – If payment is zero.
14. Display the final bill and patient classification.
15. Stop the program.

## 3. Flowchart
flowchart TD
```mermaid
    A([Start]) --> B[/Enter patient details/]
    B --> C[/Enter consultation, diagnostic and treatment charges/]
    C --> D{Are charges valid?}
    D -->|No| E[/Display Invalid Charges/]
    E --> Z([Stop])
    D -->|Yes| F[Calculate Total Bill]
    F --> G{Age >= 60?}
    G -->|Yes| H[Apply 10% Concession]
    G -->|No| I[No Age Concession]
    H --> J{Total Bill > 10000?}
    I --> J
    J -->|Yes| K[Apply 5% Concession]
    J -->|No| L[No Extra Concession]
    K --> M[Calculate Final Bill]
    L --> M
    M --> N[/Enter Amount Paid/]
    N --> O{Payment Valid?}
    O -->|No| P[/Display Invalid Payment/]
    P --> Z
    O -->|Yes| Q{Payment == Final Bill?}
    Q -->|Yes| R[Fully Paid]
    Q -->|No| S{Payment > 0?}
    S -->|Yes| T[Partially Paid]
    S -->|No| U[Pending]
    R --> V[/Display Bill Details/]
    T --> V
    U --> V
    V --> Z
```
## 5. Sample Input

```
HOSPITAL BILLING SYSTEM

Enter patient name: Ravi
Enter patient age: 65
Enter consultation charges: 2000
Enter diagnostic charges: 3000
Enter treatment charges: 7000
Enter amount paid: 5000
```

## 6. Sample Output

```
HOSPITAL BILLING SYSTEM

Total Bill: 12000.0
Concession: 1800.0
Final Bill: 10200.0

--- HOSPITAL BILL ---

Patient Name: Ravi
Age: 65
Consultation Charges: 2000.0
Diagnostic Charges: 3000.0
Treatment Charges: 7000.0

Total Bill: 12000.0
Concession: 1800.0
Final Bill: 10200.0
Amount Paid: 5000.0
Balance Amount: 5200.0
Payment Status: Partially Paid
```


