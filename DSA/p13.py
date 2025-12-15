def get_positive_float(prompt):
    """Validates and returns a positive float value."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❌ Value cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input! Enter a valid number.")


def calculate_tax(taxable_income):
    tax = 0
    breakdown = []

    # Tax slabs under New Regime (2023)
    slabs = [
        (300000, 0.00),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
        (float("inf"), 0.30)
    ]

    remaining = taxable_income

    for limit, rate in slabs:
        if remaining <= 0:
            break
        taxable_at_rate = min(remaining, limit)
        tax_amount = taxable_at_rate * rate
        breakdown.append((taxable_at_rate, rate, tax_amount))
        tax += tax_amount
        remaining -= taxable_at_rate

    # Apply Section 87A rebate
    rebate = 0
    if taxable_income <= 700000:
        rebate = tax  # full tax rebate
        tax = 0

    # Add 4% cess on tax (after rebate)
    cess = tax * 0.04
    total_tax = tax + cess

    return breakdown, rebate, cess, total_tax


def main():
    print("=== Tax & Rebate Calculator (2023 New Regime) ===")

    taxable_income = get_positive_float("Enter Taxable Income (₹): ")

    breakdown, rebate, cess, total_tax = calculate_tax(taxable_income)

    # Display results
    print("\n=========== TAX BREAKDOWN ===========")
    print(f"Taxable Income: ₹{taxable_income:,.2f}\n")

    print("Slab-wise Tax Calculation:")
    for amount, rate, tax_amt in breakdown:
        print(f"Taxed ₹{amount:,.2f} at {int(rate*100)}% → ₹{tax_amt:,.2f}")

    print("\nSection 87A Rebate:", f"₹{rebate:,.2f}")
    print("Health & Education Cess (4%):", f"₹{cess:,.2f}")
    print("--------------------------------------")
    print(f"Total Tax Payable: ₹{total_tax:,.2f}")
    print("=======================================")


main()
