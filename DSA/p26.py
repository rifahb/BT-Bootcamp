# Coding Challenge 26: Iterative Item Entry and Grand Total

grand_total = 0

while True:
    print("\nEnter item details:")
    code = input("Item code: ")
    desc = input("Description: ")
    qty = int(input("Quantity: "))
    price = float(input("Price per item: "))

    total = qty * price
    grand_total += total

    print("Item Total =", total)

    cont = input("Add another item? (y/n): ").lower()
    if cont != 'y':
        break

print("\nGrand Total for all items:", grand_total)
