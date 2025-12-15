# Coding Challenge 32: Minimum Purchase Requirement

grand_total = float(input("Enter final grand total after all adjustments: "))

if grand_total < 500:
    print("Minimum purchase of ₹500 is required. Invoice cannot be generated.")
else:
    print("Invoice generated successfully.")
    print("Final Grand Total:", grand_total)
