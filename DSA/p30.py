# Coding Challenge 30: Promotional Discounts on Specific Items

PROMO_CODE = "PROMO10"

grand_total = 0

while True:
    print("\nEnter item details:")
    code = input("Item code: ")
    desc = input("Description: ")
    qty = int(input("Quantity: "))
    price = float(input("Price: "))

    total = qty * price

    # Apply promotional discount
    if code == PROMO_CODE:
        print("Promotional 10% discount applied!")
        total = total * 0.90

    grand_total += total
    print("Item Total:", total)

    cont = input("Add another item? (y/n): ").lower()
    if cont != 'y':
        break

print("\n--- Final Grand Total ---")
print("Grand Total =", grand_total)
