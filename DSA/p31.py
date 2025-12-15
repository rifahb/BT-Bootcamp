# Coding Challenge 31: Payment Mode Rules

final_total = float(input("Enter final grand total after all discounts: "))

print("\nSelect Payment Method:")
print("1. Cash")
print("2. Credit Card")
choice = int(input("Enter option (1/2): "))

surcharge = 0

if choice == 2:
    surcharge = final_total * 0.02
    print("2% Credit Card surcharge applied.")

payable = final_total + surcharge

print("\n--- Payment Summary ---")
print("Payment Method :", "Credit Card" if choice == 2 else "Cash")
print("Surcharge      :", surcharge)
print("Final Payable  :", payable)
