## 1. Problem Statement

Develop a Python program to calculate hospital bills based on consultation charges, diagnostic charges, and treatment charges. Apply concessions based on patient category and validate billing constraints.

The program should:

- Accept patient details and hospital charges.
- Calculate the total bill.
- Apply a 10% concession for senior citizens (age 60 or above).
- Apply a 5% concession for patients with bills above ₹10,000.
- Calculate the final payable amount.
- Classify patients according to their payment status as Paid, Partially Paid, or Pending.

## 2. Algorithm

1. Start the program.
2. Enter patient name and age.
3. Enter consultation charges.
4. Enter diagnostic charges.
5. Enter treatment charges.
6. Enter the amount paid by the patient.
7. Calculate the total bill.
8. Check concession conditions:
   - If age is 60 or above, apply 10% concession.
   - If total bill is above ₹10,000, apply 5% concession.
9. Calculate the final bill after concession.
10. Validate the payment amount.
11. Classify the patient:
    - Paid: Full amount paid.
    - Partially Paid: Some amount paid.
    - Pending: No amount paid.
12. Display the bill details and patient classification.
13. Stop the program.

## 3. Flowchart 
  ``` mermaid
flowchart TD
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

Final Bill: 12750.0

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

Patient Classification: Partially Paid
```

Note: The correct final bill for this input is ₹10,200 (₹1,200 senior-citizen concession + ₹600 high-bill concession). The intermediate `12750.0` line in the sample should be ignored; the program actually prints ₹10,200.

