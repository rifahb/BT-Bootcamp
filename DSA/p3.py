

def get_number(prompt, allow_zero=True):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Please enter a positive number.")
                continue
            if not allow_zero and value == 0:
                print("Value cannot be zero. Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


total_amount = get_number("Enter the total amount: ", allow_zero=False)
discount_rate = get_number("Enter discount rate (%): ")


discount = (total_amount * discount_rate) / 100
final_amount = total_amount - discount

print("Discount Amount =", discount)
print("Amount to Pay After Discount =", final_amount)
