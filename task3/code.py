
print("HOSPITAL BILLING SYSTEM")

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

if age < 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid Billing Details")

else:
    total = consultation + diagnostic + treatment

    concession = 0

    if age >= 60:
        concession += total * 0.10

    if total > 10000:
        concession += total * 0.05

    final_bill = total - concession

    print("Total Bill:", total)
    print("Concession:", concession)
    print("Final Bill:", final_bill)

    paid = float(input("Enter amount paid: "))

    if paid < 0 or paid > final_bill:
        print("Invalid Payment Amount")

    else:
        balance = final_bill - paid

        if paid == final_bill:
            status = "Fully Paid"
        elif paid > 0:
            status = "Partially Paid"
        else:
            status = "Pending"

        print("\n--- HOSPITAL BILL ---")
        print("Patient Name:", name)
        print("Age:", age)
        print("Consultation Charges:", consultation)
        print("Diagnostic Charges:", diagnostic)
        print("Treatment Charges:", treatment)
        print("Total Bill:", total)
        print("Concession:", concession)
        print("Final Bill:", final_bill)
        print("Amount Paid:", paid)
        print("Balance Amount:", balance)
        print("Payment Status:", status)

