def get_positive_float(prompt):
    """Validate and return a positive float."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❌ Value cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input! Enter a valid number.")


def main():
    print("=== Net Salary Calculator ===")

    # Input values
    annual_gross = get_positive_float("Enter Annual Gross Salary (₹): ")
    total_tax_payable = get_positive_float("Enter Total Tax Payable (including cess) (₹): ")

    # Calculate Net Salary
    annual_net_salary = annual_gross - total_tax_payable

    # Output
    print("\n========== NET SALARY REPORT ==========")
    print(f"Annual Gross Salary : ₹{annual_gross:,.2f}")
    print(f"Total Tax Payable   : ₹{total_tax_payable:,.2f}")
    print(f"Annual Net Salary   : ₹{annual_net_salary:,.2f}")
    print("========================================")

# Run program
main()
