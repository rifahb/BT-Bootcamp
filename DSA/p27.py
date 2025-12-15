# Coding Challenge 27: Applying Discounts

grand_total = 0
total_qty = 0

while True:
    print("\nEnter item details:")
    code = input("Item code: ")
    desc = input("Description: ")
    qty = int(input("Quantity: "))
    price = float(input("Price per item: "))

    total = qty * price
    grand_total += total
    total_qty += qty

    cont = input("Add another item? (y/n): ").lower()
    if cont != 'y':
        break

print("\n--- Before Discounts ---")
print("Grand Total:", grand_total)
print("Total Quantity:", total_qty)

# Apply discounts
discount = 0

if grand_total > 10000:
    discount += grand_total * 0.10
    print("10% Discount Applied")

if total_qty > 20:
    extra = (grand_total - discount) * 0.05
    discount += extra
    print("Additional 5% Quantity Discount Applied")

final_total = grand_total - discount

print("\n--- After Discounts ---")
print("Total Discount Applied:", discount)
print("Grand Total After Discounts:", final_total)
