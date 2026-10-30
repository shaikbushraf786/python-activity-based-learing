Here is a complete solution for the **Multi-Plan Telecommunications Cost Optimization** problem, structured with the problem statement, algorithm, mermaid flowchart, python source code, and sample input/output.

---

### 1. Problem Statement

Given a user's projected mobile usage requirements over a billing period (Voice Minutes, Data in GB, SMS count, and a Maximum Monthly Budget) and a catalog of available telecommunications plans (each with its own base price, validity duration, included allowances, and overage/excess rates), the objective is to:

* **Normalize** usage requirements and plan costs across differing validity periods to a standard monthly equivalent.
* **Calculate Excess Charges** for voice, data, and SMS whenever usage exceeds plan allowances.
* **Evaluate Budget Constraints** to filter out plans that exceed the user's maximum budget.
* **Identify the Most Economical Plan** among the eligible options that minimizes total normalized cost.

---

### 2. Algorithm

1. **Input Collection**: Receive user requirements (Monthly Voice $V$, Data $D$, SMS $S$, and Budget $B$) and a list of available plans.
2. **Iteration and Scaling**: For each plan in the catalog:
* Calculate the **Scale Factor** based on plan validity duration ($D_{val} / 30$ days).
* Scale the user's requirements to match the plan's validity period.
* Determine **Excess Usage** ($\max(0, \text{Required} - \text{Included})$) for voice, data, and SMS.
* Compute **Excess Charges** by multiplying excess quantities by their respective overage rates.
* Calculate the **Total Period Cost** ($\text{Base Price} + \text{Excess Charges}$).
* Normalize the total period cost to a standard **Monthly Equivalent Cost** ($\frac{\text{Total Period Cost}}{\text{Validity Days}} \times 30$).


3. **Budget Filtering**: Check if $\text{Monthly Cost} \le \text{Budget}$. If true, mark the plan as **Eligible**.
4. **Optimization**: From the list of eligible plans, select the one with the minimum monthly cost.
5. **Output**: Display the evaluation report for all plans and highlight the optimal choice.

---

### 3. Flowchart (Mermaid)

```mermaid
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

```

---

### 4. Python Source Code

```python
class MobilePlan:
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

```

---

### 5. Sample Input

* **User Requirements (Monthly):**
* Voice Minutes: `300`
* Data: `25.0 GB`
* SMS: `100`
* Maximum Budget: `$35.00`


* **Plans Catalog:**
* **Plan A (Basic)**: `$15.00` / 30 days (Includes: 200m, 10GB, 50 SMS | Overage: $0.10/m, $2.00/GB, $0.05/SMS)
* **Plan B (Standard)**: `$25.00` / 30 days (Includes: 400m, 30GB, 200 SMS | Overage: $0.08/m, $1.50/GB, $0.04/SMS)
* **Plan C (Data Heavy)**: `$30.00` / 30 days (Includes: 250m, 50GB, 100 SMS | Overage: $0.12/m, $1.00/GB, $0.05/SMS)
* **Plan D (Quarterly Value)**: `$70.00` / 90 days (Includes: 1000m, 80GB, 500 SMS | Overage: $0.08/m, $1.20/GB, $0.03/SMS)



---

### 6. Sample Output

```text
=== Plan Evaluation Report ===
Plan: Plan A (Basic) [EXCEEDS BUDGET]
  - Validity: 30 days
  - Period Cost: $57.50
  - Normalized Monthly Cost: $57.50
  - Excess Charges: $42.50 (Voice: 100.0m, Data: 15.0GB, SMS: 50.0)
--------------------------------------------------
Plan: Plan B (Standard) [ELIGIBLE]
  - Validity: 30 days
  - Period Cost: $25.00
  - Normalized Monthly Cost: $25.00
  - Excess Charges: $0.00 (Voice: 0.0m, Data: 0.0GB, SMS: 0.0)
--------------------------------------------------
Plan: Plan C (Data Heavy) [EXCEEDS BUDGET]
  - Validity: 30 days
  - Period Cost: $36.00
  - Normalized Monthly Cost: $36.00
  - Excess Charges: $6.00 (Voice: 50.0m, Data: 0.0GB, SMS: 0.0)
--------------------------------------------------
Plan: Plan D (Quarterly Value) [ELIGIBLE]
  - Validity: 90 days
  - Period Cost: $70.00
  - Normalized Monthly Cost: $23.33
  - Excess Charges: $0.00 (Voice: 0.0m, Data: 0.0GB, SMS: 0.0)
--------------------------------------------------

✨ Most Economical Eligible Plan: **Plan D (Quarterly Value)** with a monthly cost of **$23.33**.

```
