def calculate_tax(taxable_income):
    tax = 0

    if taxable_income > 1000000:
        tax += (taxable_income - 1000000) * 0.30
        taxable_income = 1000000

    if taxable_income > 500000:
        tax += (taxable_income - 500000) * 0.20
        taxable_income = 500000

    if taxable_income > 250000:
        tax += (taxable_income - 250000) * 0.05

    cess = tax * 0.04
    return tax, cess


def generate_report(name, emp_id, gross_monthly_salary):
    annual_gross = gross_monthly_salary * 12
    taxable_income = max(annual_gross - 50000, 0)

    tax, cess = calculate_tax(taxable_income)
    total_tax = tax + cess
    net_salary = annual_gross - total_tax

    print("\n------------------------------------------------------------")
    print("                    EMPLOYEE TAX REPORT")
    print("------------------------------------------------------------")
    print(f"Name:                         {name}")
    print(f"EmpID:                        {emp_id}")
    print(f"Gross Monthly Salary:         ₹{gross_monthly_salary:,}")
    print(f"Annual Gross Salary:          ₹{annual_gross:,}")
    print("------------------------------------------------------------")
    print("Tax Computation Breakdown")
    print("------------------------------------------------------------")
    print(f"Taxable Income:               ₹{taxable_income:,}")
    print(f"Tax Before Cess:              ₹{tax:,.2f}")
    print(f"Health & Education Cess:      ₹{cess:,.2f}")
    print("------------------------------------------------------------")
    print(f"Total Tax Payable:            ₹{total_tax:,.2f}")
    print(f"Annual Net Salary:            ₹{net_salary:,.2f}")
    print("------------------------------------------------------------\n")


# ---------------- Example ---------------- #
generate_report("John Doe", "E12345", 85000)
