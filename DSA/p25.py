# Coding Challenge 25: Basic Item Entry and Total Calculation

code = input("Enter item code: ")
desc = input("Enter item description: ")
qty = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total = qty * price

print("\n--- Item Total ---")
print("Item Code      :", code)
print("Description    :", desc)
print("Quantity       :", qty)
print("Price per Item :", price)
print("Total Cost     :", total)
