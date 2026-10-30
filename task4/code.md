flowchart TD
    A[Start: Input User Usage & Budget, Plan Catalog] --> B[Initialize Eligible Plans List]
    B --> C{More Plans in Catalog?}
    C -- Yes --> D[Fetch Next Plan Details]
    D --> E[Scale User Requirements to Plan Validity]
    E --> F[Calculate Excess Voice, Data, & SMS]
    F --> G[Calculate Excess Charges & Total Plan Cost]
    G --> H[Normalize Total Cost to Monthly Equivalent]
    H --> I{Normalized Cost <= Budget?}
    I -- Yes --> J[Mark Plan as Eligible & Add to List]
    I -- No --> K[Mark Plan as Ineligible]
    J --> C
    K --> C
    C -- No --> L{Any Eligible Plans Found?}
    L -- No --> M[Output: No Eligible Plan Within Budget]
    L -- Yes --> N[Find Plan with Minimum Monthly Cost]
    N --> O[Output Optimal Plan & Cost Breakdown]
    M --> P[End]
    O --> P
    Here is the detailed step-by-step **Algorithm** for the Multi-Plan Telecommunications Cost Optimization system:

---

### **Algorithm: Telecommunications Cost Optimization**

#### **Phase 1: Input Initialization**

1. **Input User Requirements:**
* Monthly Voice Minutes ($V_{req}$)
* Monthly Data Allowance in GB ($D_{req}$)
* Monthly SMS Count ($S_{req}$)
* Maximum Monthly Budget ($B_{max}$)


2. **Input Catalog:**
* A list of available mobile plans ($P$), where each plan $p \in P$ contains:
* Name ($p_{name}$)
* Base Price ($p_{price}$)
* Validity Period in days ($p_{days}$)
* Included Voice Minutes ($p_{iv}$)
* Included Data in GB ($p_{id}$)
* Included SMS Count ($p_{is}$)
* Overage Rate per excess Voice Minute ($p_{rv}$)
* Overage Rate per excess GB of Data ($p_{rd}$)
* Overage Rate per excess SMS ($p_{rs}$)




3. **Initialize Collections:**
* Create an empty list `evaluation_results` to store computation outcomes for each plan.
* Set standard monthly normalization constant: $M_{days} = 30.0$ days.



---

#### **Phase 2: Plan Evaluation and Normalization Loop**

For each plan $p$ in the catalog $P$:

1. **Scale User Requirements to Plan Validity:**
* Calculate the duration scale factor: $\text{Scale} = \frac{p_{days}}{M_{days}}$
* Compute required consumption for the plan's specific validity period:
* $\text{Req}_V = V_{req} \times \text{Scale}$
* $\text{Req}_D = D_{req} \times \text{Scale}$
* $\text{Req}_S = S_{req} \times \text{Scale}$




2. **Calculate Excess Usage:**
* $\text{Excess}_V = \max(0, \text{Req}_V - p_{iv})$
* $\text{Excess}_D = \max(0, \text{Req}_D - p_{id})$
* $\text{Excess}_S = \max(0, \text{Req}_S - p_{is})$


3. **Calculate Costs:**
* Compute Total Overage Charges:

$$\text{ExcessCost} = (\text{Excess}_V \times p_{rv}) + (\text{Excess}_D \times p_{rd}) + (\text{Excess}_S \times p_{rs})$$


* Compute Total Plan Cost for the Validity Period:

$$\text{PeriodCost} = p_{price} + \text{ExcessCost}$$


* Normalize Cost to a Standard Monthly Equivalent:

$$\text{MonthlyCost} = \left(\frac{\text{PeriodCost}}{p_{days}}\right) \times M_{days}$$




4. **Apply Budget Constraint Filter:**
* If $\text{MonthlyCost} \le B_{max}$:
* Mark plan status as **Eligible** ($\text{IsEligible} = \text{True}$)


* Else:
* Mark plan status as **Ineligible / Exceeds Budget** ($\text{IsEligible} = \text{False}$)




5. **Store Results:**
* Append plan details, calculated excess values, period cost, normalized monthly cost, and eligibility status to `evaluation_results`.



---

#### **Phase 3: Optimal Plan Selection & Output**

1. **Filter Eligible Options:**
* Extract all plans from `evaluation_results` where $\text{IsEligible} == \text{True}$.


2. **Find Most Economical Plan:**
* If the list of eligible plans is **not empty**:
* Select the plan with the **minimum** `MonthlyCost`.
* Designate this plan as the **Optimal Plan**.


* Else:
* Flag that no plans meet the budget criteria.




3. **Display Output:**
* Print the complete evaluation report for all evaluated plans.
* Highlight the optimal plan name and its normalized monthly cost, or display a budget warning message if no eligible plans were found.
* class MobilePlan:
    def __init__(self, name, base_price, validity_days, inc_voice, inc_data, inc_sms, rate_voice, rate_data, rate_sms):
        self.name = name
        self.base_price = base_price          # Base price for the validity period
        self.validity_days = validity_days    # Validity duration in days
        self.inc_voice = inc_voice            # Included voice minutes
        self.inc_data = inc_data              # Included data in GB
        self.inc_sms = inc_sms                # Included SMS count
        self.rate_voice = rate_voice          # Cost per excess minute
        self.rate_data = rate_data            # Cost per excess GB
        self.rate_sms = rate_sms              # Cost per excess SMS

def evaluate_plans(user_usage, plans):
    """
    Evaluates mobile plans against user usage and budget.
    user_usage: dict with keys 'voice', 'data', 'sms', 'budget' (monthly basis / 30 days)
    """
    results = []
    monthly_days = 30.0
    
    for plan in plans:
        # Scale user requirements to the plan's validity duration
        scale_factor = plan.validity_days / monthly_days
        required_voice = user_usage['voice'] * scale_factor
        required_data = user_usage['data'] * scale_factor
        required_sms = user_usage['sms'] * scale_factor
        
        # Calculate excess usage
        excess_voice = max(0.0, required_voice - plan.inc_voice)
        excess_data = max(0.0, required_data - plan.inc_data)
        excess_sms = max(0.0, required_sms - plan.inc_sms)
        
        # Calculate excess charges
        excess_cost = (
            excess_voice * plan.rate_voice +
            excess_data * plan.rate_data +
            excess_sms * plan.rate_sms
        )
        
        total_plan_cost = plan.base_price + excess_cost
        
        # Normalize to monthly cost for fair comparison
        monthly_cost = (total_plan_cost / plan.validity_days) * monthly_days
        
        # Check budget constraint
        is_eligible = monthly_cost <= user_usage['budget']
        
        results.append({
            'plan_name': plan.name,
            'validity_days': plan.validity_days,
            'total_period_cost': total_plan_cost,
            'monthly_cost': monthly_cost,
            'excess_voice': excess_voice,
            'excess_data': excess_data,
            'excess_sms': excess_sms,
            'excess_cost': excess_cost,
            'is_eligible': is_eligible
        })
        
    return results

def find_optimal_plan(user_usage, plans):
    evaluations = evaluate_plans(user_usage, plans)
    eligible_plans = [p for p in evaluations if p['is_eligible']]
    
    optimal = None
    if eligible_plans:
        optimal = min(eligible_plans, key=lambda x: x['monthly_cost'])
        
    return evaluations, optimal

# --- Sample Execution ---
if __name__ == "__main__":
    # User monthly requirements and budget
    user_requirements = {
        'voice': 300,    # minutes per month
        'data': 25.0,    # GB per month
        'sms': 100,      # SMS per month
        'budget': 35.0   # Maximum monthly budget ($)
    }
    
    # Available plan catalog
    available_plans = [
        MobilePlan("Plan A (Basic)", base_price=15.0, validity_days=30, inc_voice=200, inc_data=10.0, inc_sms=50, rate_voice=0.10, rate_data=2.00, rate_sms=0.05),
        MobilePlan("Plan B (Standard)", base_price=25.0, validity_days=30, inc_voice=400, inc_data=30.0, inc_sms=200, rate_voice=0.08, rate_data=1.50, rate_sms=0.04),
        MobilePlan("Plan C (Data Heavy)", base_price=30.0, validity_days=30, inc_voice=250, inc_data=50.0, inc_sms=100, rate_voice=0.12, rate_data=1.00, rate_sms=0.05),
        MobilePlan("Plan D (Quarterly Value)", base_price=70.0, validity_days=90, inc_voice=1000, inc_data=80.0, inc_sms=500, rate_voice=0.08, rate_data=1.20, rate_sms=0.03)
    ]
    
    evaluations, optimal_plan = find_optimal_plan(user_requirements, available_plans)
    
    print("=== Plan Evaluation Report ===")
    for eval_res in evaluations:
        status = "ELIGIBLE" if eval_res['is_eligible'] else "EXCEEDS BUDGET"
        print(f"Plan: {eval_res['plan_name']} [{status}]")
        print(f"  - Validity: {eval_res['validity_days']} days")
        print(f"  - Period Cost: ${eval_res['total_period_cost']:.2f}")
        print(f"  - Normalized Monthly Cost: ${eval_res['monthly_cost']:.2f}")
        print(f"  - Excess Charges: ${eval_res['excess_cost']:.2f} (Voice: {eval_res['excess_voice']:.1f}m, Data: {eval_res['excess_data']:.1f}GB, SMS: {eval_res['excess_sms']:.1f})")
        print("-" * 50)
        
    if optimal_plan:
        print(f"\n✨ Most Economical Eligible Plan: **{optimal_plan['plan_name']}** with a monthly cost of **${optimal_plan['monthly_cost']:.2f}**.")
    else:
        print("\n⚠️ No plans found within the specified budget constraint.")
