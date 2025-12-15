# Coding Challenge 28: Membership Discounts

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

discount = 0

# Regular discounts
if grand_total > 10000:
    discount += grand_total * 0.10

if total_qty > 20:
    discount += (grand_total - discount) * 0.05

amount_after_discounts = grand_total - discount

# Membership discount
member = input("Is the customer a member? (y/n): ").lower()
if member == 'y':
    mem_discount = amount_after_discounts * 0.02
    discount += mem_discount
    print("Membership Discount Applied (2%)")

final_total = grand_total - discount

print("\n--- Final Total After All Discounts ---")
print("Total Discount:", discount)
print("Final Grand Total:", final_total)
