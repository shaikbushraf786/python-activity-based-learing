class Passenger:
    def __init__(self, name, age, travel_class, distance_km, is_cancelled=False):
        self.name = name
        self.age = age
        self.travel_class = travel_class
        self.distance_km = distance_km
        self.is_cancelled = is_cancelled

def calculate_railway_fares(passengers):
    # Rate configuration per KM and fixed reservation fees per class
    class_rates = {
        'Sleeper': 1.50,
        'AC_3Tier': 2.75,
        'AC_2Tier': 3.80,
        'First_AC': 5.00
    }
    
    reservation_fees = {
        'Sleeper': 20.0,
        'AC_3Tier': 40.0,
        'AC_2Tier': 50.0,
        'First_AC': 60.0
    }
    
    print(f"{'Passenger Name':<15} | {'Class':<10} | {'Base Fare':<10} | {'Concession':<10} | {'Resv Fee':<10} | {'Final Fare':<10} | {'Status':<10}")
    print("-" * 88)
    
    total_group_fare = 0.0
    
    for p in passengers:
        if p.travel_class not in class_rates:
            print(f"Error: Invalid travel class '{p.travel_class}' for {p.name}")
            continue
            
        # 1. Base Fare Calculation
        base_fare = p.distance_km * class_rates[p.travel_class]
        
        # 2. Age-Based Concession
        concession_rate = 0.0
        if p.age < 5:
            concession_rate = 1.00  # 100% off (Free)
        elif p.age >= 60:
            concession_rate = 0.40  # 40% off for senior citizens
            
        concession_amount = base_fare * concession_rate
        discounted_base = base_fare - concession_amount
        
        # 3. Reservation Fee
        res_fee = reservation_fees[p.travel_class] if p.age >= 5 else 0.0
        
        # 4. Total Ticket Fare
        ticket_fare = discounted_base + res_fee
        
        # 5. Cancellation Logic
        status = "Confirmed"
        if p.is_cancelled:
            status = "Cancelled"
            penalty = 50.0  # Flat cancellation fee
            refund = max(0, ticket_fare - penalty)
            ticket_fare = 0.0 # Billed amount becomes zero, refund processed separately
            
        total_group_fare += ticket_fare
        
        print(f"{p.name:<15} | {p.travel_class:<10} | ${base_fare:<9.2f} | ${concession_amount:<9.2f} | ${res_fee:<9.2f} | ${ticket_fare:<9.2f} | {status:<10}")
        
    print("-" * 88)
    print(f"💰 **Total Group Railway Fare:** ${total_group_fare:.2f}")

# --- Sample Execution ---
if __name__ == "__main__":
    # Sample Passenger List
    passenger_list = [
        Passenger("Alice Smith", 28, "AC_3Tier", 450, is_cancelled=False),
        Passenger("Bob Jones", 65, "Sleeper", 300, is_cancelled=False),       # Senior Citizen
        Passenger("Charlie Brown", 3, "AC_2Tier", 800, is_cancelled=False),    # Infant (<5 free)
        Passenger("Diana Prince", 45, "First_AC", 1200, is_cancelled=True)     # Cancelled ticket
    ]
    
    calculate_railway_fares(passenger_list)
