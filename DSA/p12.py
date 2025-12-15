def get_positive_float(prompt):
    """Validates and returns a positive float value."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Enter a number.")


def main():
    print("=== Taxable Income Calculator ===")

    annual_gross_salary = get_positive_float("Enter Annual Gross Salary (₹): ")

    STANDARD_DEDUCTION = 50000

    taxable_income = annual_gross_salary - STANDARD_DEDUCTION
    if taxable_income < 0:
        taxable_income = 0 

    print("\n======= TAXABLE INCOME REPORT =======")
    print(f"Annual Gross Salary : ₹{annual_gross_salary:,.2f}")
    print(f"Standard Deduction  : ₹{STANDARD_DEDUCTION:,.2f}")
    print(f"Taxable Income      : ₹{taxable_income:,.2f}")
    print("=====================================")

main()
