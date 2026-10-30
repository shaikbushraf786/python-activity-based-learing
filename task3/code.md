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

## 3. Flowchart (Mermaid Code)

\#chatgpt-mermaid-\_r_er\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_er\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_er\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_er\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_er\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_er\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_er\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_er\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_er\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_er\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_er\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_er\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_er\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_er\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_er\_ p{margin:0;}#chatgpt-mermaid-\_r_er\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_er\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_er\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_er\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_er\_ .label text,#chatgpt-mermaid-\_r_er\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_er\_ .node rect,#chatgpt-mermaid-\_r_er\_ .node circle,#chatgpt-mermaid-\_r_er\_ .node ellipse,#chatgpt-mermaid-\_r_er\_ .node polygon,#chatgpt-mermaid-\_r_er\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_er\_ .rough-node .label text,#chatgpt-mermaid-\_r_er\_ .node .label text,#chatgpt-mermaid-\_r_er\_ .image-shape .label,#chatgpt-mermaid-\_r_er\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_er\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_er\_ .rough-node .label,#chatgpt-mermaid-\_r_er\_ .node .label,#chatgpt-mermaid-\_r_er\_ .image-shape .label,#chatgpt-mermaid-\_r_er\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_er\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_er\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_er\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_er\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_er\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_er\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_er\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_er\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_er\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_er\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_er\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_er\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_er\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_er\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_er\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_er\_ .icon-shape,#chatgpt-mermaid-\_r_er\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_er\_ .icon-shape p,#chatgpt-mermaid-\_r_er\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_er\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_er\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_er\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_er\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_er\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_er\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_er\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_er\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_er\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_er\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_er\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_er\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_er\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_er\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_er\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_er\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_er\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_er\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_er\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_er\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_er\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_er\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_er\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_er\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_er\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_er\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_er\_ .node rect,#chatgpt-mermaid-\_r_er\_ .node circle,#chatgpt-mermaid-\_r_er\_ .node ellipse,#chatgpt-mermaid-\_r_er\_ .node polygon,#chatgpt-mermaid-\_r_er\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_er\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_er\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_er\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_er\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_er\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter patient detailsEnter consultation, diagnosticand treatment chargesAre charges valid?Display Invalid ChargesStopCalculate Total BillAge = 60?Apply 10% ConcessionNo Age ConcessionTotal Bill 10000?Apply 5% ConcessionNo Extra ConcessionCalculate Final BillEnter Amount PaidPayment Valid?Display Invalid PaymentPayment == Final Bill?Fully PaidPayment 0?Partially PaidPendingDisplay Bill DetailsNoYesYesNoYesNoNoYesYesNoYesNo

## 4. Python Source Code (Without Comments)

```
print("HOSPITAL BILLING SYSTEM")name = input("Enter patient name: ")age = int(input("Enter patient age: "))consultation = float(input("Enter consultation charges: "))diagnostic = float(input("Enter diagnostic charges: "))treatment = float(input("Enter treatment charges: "))if age < 0 or consultation < 0 or diagnostic < 0 or treatment < 0:    print("Invalid Billing Details")else:    total = consultation + diagnostic + treatment    concession = 0    if age >= 60:        concession += total * 0.10    if total > 10000:        concession += total * 0.05    final_bill = total - concession    print("Total Bill:", total)    print("Concession:", concession)    print("Final Bill:", final_bill)    paid = float(input("Enter amount paid: "))    if paid < 0 or paid > final_bill:        print("Invalid Payment Amount")    else:        balance = final_bill - paid        if paid == final_bill:            status = "Fully Paid"        elif paid > 0:            status = "Partially Paid"        else:            status = "Pending"        print("\n--- HOSPITAL BILL ---")        print("Patient Name:", name)        print("Age:", age)        print("Consultation Charges:", consultation)        print("Diagnostic Charges:", diagnostic)        print("Treatment Charges:", treatment)        print("Total Bill:", total)        print("Concession:", concession)        print("Final Bill:", final_bill)        print("Amount Paid:", paid)        print("Balance Amount:", balance)        print("Payment Status:", status)
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

## 7. Result

Thus, the Python program successfully calculates hospital bills, applies conditional concessions, validates billing constraints, and classifies patients based on their payment status.
    
