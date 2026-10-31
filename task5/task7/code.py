# Progressive Water Tariff Analysis

## 1. Problem Statement

Develop a Python program to calculate water bills for multiple households based on their monthly water consumption. The program should apply progressive tariff rates for different consumption slabs, add fixed monthly charges, and calculate penalties for excessive usage. It should compare household consumption patterns, calculate the total bill for each household, and identify households with excessive water consumption.

## 2. Algorithm

1. Start the program.
2. Read the number of households.
3. Set the water tariff rates:
   - First 100 litres: ₹2 per litre.
   - Next 100 litres: ₹3 per litre.
   - Above 200 litres: ₹5 per litre.
4. Set the fixed monthly fee as ₹50.
5. Read each household's name and water consumption.
6. Calculate the water charge based on consumption slabs.
7. Add the fixed monthly fee.
8. If consumption exceeds 250 litres, add a penalty of ₹100.
9. Calculate the final bill.
10. Display each household's consumption and bill.
11. Compare household consumption.
12. Identify the household with the highest consumption.
13. Display households with excessive usage.
14. Stop the program.

## 3. Flowchart

flowchart TD
    A([Start]) --> B[/Enter number of households/]
    B --> C[Set fixed fee = 50<br/>Penalty = 100]
    C --> D[Set household counter = 1]
    D --> E{Counter <= Number of households?}

    E -- Yes --> F[/Enter household name<br/>and water consumption/]

    F --> G{Consumption <= 100?}

    G -- Yes --> H[Bill = Consumption * 2]

    G -- No --> I{Consumption <= 200?}

    I -- Yes --> J[Bill = 200 + (Consumption - 100) * 3]

    I -- No --> K[Bill = 500 + (Consumption - 200) * 5]

    H --> L[Add fixed fee]
    J --> L
    K --> L

    L --> M{Consumption > 250?}

    M -- Yes --> N[Add penalty = 100]
    M -- No --> O[Calculate final bill]

    N --> O

    O --> P[/Display household bill/]

    P --> Q{Consumption > 250?}

    Q -- Yes --> R[Display Excessive Usage]
    Q -- No --> S[Display Normal Usage]

    R --> T[Update highest consumption]
    S --> T

    T --> U[Increment counter]
    U --> E

    E -- No --> V[Display highest consumption<br/>and household name]
    V --> W([Stop])

[Solved Open with (C) The following flowchart shows an | Chegg.com](https://images.openai.com/static-rsc-4/4ZR9L9TqoMsO6Erq_EOxPrQ47RBsfw2y3EU1OX7kcIyq_mMouqcvm4tR1SewRBqMsuhqUi3CwnkPFx4uFN-pO2UIyyoIBp23SqV0K-IFZDpOZTOAUKlWmGmBHvKlunnrp_VkmZx3NuHlAHsopDU6wlda---mtHsKy9H2E7I6874?purpose=inline)

[chegg.com](https://www.chegg.com/homework-help/questions-and-answers/open-c-following-flowchart-shows-algorithm-calculates-displays-water-bill-10-users-algorit-q91316114?utm_source=chatgpt.com)

## 4. Python Source Code

```
# Progressive Water Tariff Analysisn = int(input("Enter number of households: "))fixed_fee = 50penalty = 100highest = 0highest_name = ""for i in range(n):    print("\nHousehold", i + 1)    name = input("Enter household name: ")    units = int(input("Enter water consumption: "))    # Calculate progressive water charges    if units <= 100:        bill = units * 2    elif units <= 200:        bill = (100 * 2) + (units - 100) * 3    else:        bill = (100 * 2) + (100 * 3) + (units - 200) * 5    # Add fixed fee    bill = bill + fixed_fee    # Apply excessive usage penalty    if units > 250:        bill = bill + penalty    print("Household Name:", name)    print("Water Consumption:", units)
```

## 5. Sample Input

```
Enter number of households: 3

Household 1
Enter household name: Ali
Enter water consumption: 80

Household 2
Enter household name: Ravi
Enter water consumption: 180

Household 3
Enter household name: Sara
Enter water consumption: 300
```

## 6. Sample Output

```
Household Name: Ali
Water Consumption: 80
Total Water Bill: Rs. 210
Status: Normal Usage

Household Name: Ravi
Water Consumption: 180
Total Water Bill: Rs. 490
Status: Normal Usage

Household Name: Sara
Water Consumption: 300
Total Water Bill: Rs. 1050
Status: Excessive Usage

--- Consumption Analysis ---
Highest Consumption: 300
Household: Sara
Excessive usage limit: 250 litres
```

## 7. Flowchart in Mermaid Code

Copy this code into the Mermaid Live Editor to generate your flowchart.

\#chatgpt-mermaid-\_r_b4\_-healed{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_b4\_-healed .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_b4\_-healed .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_b4\_-healed .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_b4\_-healed .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_b4\_-healed .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_b4\_-healed .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_b4\_-healed .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_b4\_-healed .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_b4\_-healed .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_b4\_-healed .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_b4\_-healed .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_b4\_-healed .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_b4\_-healed svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_b4\_-healed p{margin:0;}#chatgpt-mermaid-\_r_b4\_-healed .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_b4\_-healed .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_b4\_-healed .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_b4\_-healed .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_b4\_-healed .label text,#chatgpt-mermaid-\_r_b4\_-healed span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_b4\_-healed .node rect,#chatgpt-mermaid-\_r_b4\_-healed .node circle,#chatgpt-mermaid-\_r_b4\_-healed .node ellipse,#chatgpt-mermaid-\_r_b4\_-healed .node polygon,#chatgpt-mermaid-\_r_b4\_-healed .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_b4\_-healed .rough-node .label text,#chatgpt-mermaid-\_r_b4\_-healed .node .label text,#chatgpt-mermaid-\_r_b4\_-healed .image-shape .label,#chatgpt-mermaid-\_r_b4\_-healed .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_b4\_-healed .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_b4\_-healed .rough-node .label,#chatgpt-mermaid-\_r_b4\_-healed .node .label,#chatgpt-mermaid-\_r_b4\_-healed .image-shape .label,#chatgpt-mermaid-\_r_b4\_-healed .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_b4\_-healed .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_b4\_-healed .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_b4\_-healed .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_b4\_-healed .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_b4\_-healed .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_b4\_-healed .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_b4\_-healed .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_b4\_-healed .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_b4\_-healed .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_b4\_-healed .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_b4\_-healed .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_b4\_-healed .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_b4\_-healed div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_b4\_-healed .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_b4\_-healed rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_b4\_-healed .icon-shape,#chatgpt-mermaid-\_r_b4\_-healed .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_b4\_-healed .icon-shape p,#chatgpt-mermaid-\_r_b4\_-healed .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_b4\_-healed .icon-shape .label rect,#chatgpt-mermaid-\_r_b4\_-healed .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_b4\_-healed .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_b4\_-healed .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_b4\_-healed .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_b4\_-healed [data-look="neo"].node rect,#chatgpt-mermaid-\_r_b4\_-healed [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_b4\_-healed [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_b4\_-healed-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_b4\_-healed [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_b4\_-healed [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_b4\_-healed-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_b4\_-healed [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_b4\_-healed [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_b4\_-healed [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_b4\_-healed-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_b4\_-healed [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_b4\_-healed [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_b4\_-healed-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_b4\_-healed [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_b4\_-healed-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_b4\_-healed .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_b4\_-healed .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_b4\_-healed .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_b4\_-healed .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_b4\_-healed .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_b4\_-healed .node rect,#chatgpt-mermaid-\_r_b4\_-healed .node circle,#chatgpt-mermaid-\_r_b4\_-healed .node ellipse,#chatgpt-mermaid-\_r_b4\_-healed .node polygon,#chatgpt-mermaid-\_r_b4\_-healed .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_b4\_-healed .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_b4\_-healed .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_b4\_-healed .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_b4\_-healed .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_b4\_-healed :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of householdsSet fixed fee = 50Penalty = 100Set household counter = 1Counter <= Number ofhouseholds?Enter household nameand water consumptionConsumption <= 100?Bill = Consumption \* 2Consumption <= 200?Bill = 200 + (Consumption -100) \* 3Bill = 500 + (Consumption -200) \* 5Add fixed feeConsumption 250?Add penalty = 100Calculate final billDisplay household billConsumption 250?Display Excessive UsageDisplay Normal UsageUpdate highest consumptionIncrement counterDisplay highest consumptionand household nameStopYesYesNoYesNoYesNoYesNoNo

Note: All tariff rates and the penalty are assumed values for this programming exercise. The program uses progressive slab calculations, meaning each slab is charged at its own rate.
