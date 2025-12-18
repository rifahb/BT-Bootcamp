# ============================================
# GlobalNext Solutions - Tax Calculator
# New Tax Regime (FY 2023-24)
# ============================================

STANDARD_DEDUCTION = 50000
REBATE_LIMIT = 700000
CESS_RATE = 0.04


def validate_amount(value, field_name):
    """Validate salary inputs"""
    if value < 0:
        raise ValueError(f"{field_name} cannot be negative")
    return value


def calculate_tax_new_regime(taxable_income):
    """Calculate tax using New Tax Regime slabs"""

    slabs = [
        (300000, 0.00),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
        (float("inf"), 0.30)
    ]

    remaining_income = taxable_income
    tax = 0
    breakdown = []

    for limit, rate in slabs:
        if remaining_income <= 0:
            break

        slab_income = min(remaining_income, limit)
        slab_tax = slab_income * rate

        breakdown.append({
            "Slab Income": slab_income,
            "Rate": f"{int(rate * 100)}%",
            "Tax": slab_tax
        })

        tax += slab_tax
        remaining_income -= slab_income

    # Section 87A Rebate
    rebate = tax if taxable_income <= REBATE_LIMIT else 0
    tax_after_rebate = tax - rebate

    # Health & Education Cess
    cess = tax_after_rebate * CESS_RATE
    total_tax = tax_after_rebate + cess

    return breakdown, rebate, cess, total_tax


def generate_tax_report(emp_id, emp_name, basic, hra, allowances):
    """Generate complete employee tax report"""

    # Validate inputs
    basic = validate_amount(basic, "Basic Salary")
    hra = validate_amount(hra, "HRA")
    allowances = validate_amount(allowances, "Allowances")

    # Gross Salary Calculation
    monthly_gross = basic + hra + allowances
    annual_gross = monthly_gross * 12

    # Taxable Income
    taxable_income = max(0, annual_gross - STANDARD_DEDUCTION)

    # Tax Calculation
    breakdown, rebate, cess, total_tax = calculate_tax_new_regime(taxable_income)

    # Net Salary
    net_salary = annual_gross - total_tax

    return {
        "Employee ID": emp_id,
        "Employee Name": emp_name,
        "Monthly Gross Salary": monthly_gross,
        "Annual Gross Salary": annual_gross,
        "Standard Deduction": STANDARD_DEDUCTION,
        "Taxable Income": taxable_income,
        "Tax Breakdown": breakdown,
        "Rebate (Section 87A)": rebate,
        "Health & Education Cess": cess,
        "Total Tax Payable": total_tax,
        "Net Annual Salary": net_salary
    }


def display_report(report):
    """Display formatted tax report"""

    print("\n" + "=" * 50)
    print("        GLOBALNEXT SOLUTIONS TAX REPORT")
    print("=" * 50)

    print(f"Employee ID       : {report['Employee ID']}")
    print(f"Employee Name     : {report['Employee Name']}")
    print(f"Monthly Gross     : ₹{report['Monthly Gross Salary']:.2f}")
    print(f"Annual Gross      : ₹{report['Annual Gross Salary']:.2f}")
    print(f"Standard Deduction: ₹{report['Standard Deduction']:.2f}")
    print(f"Taxable Income    : ₹{report['Taxable Income']:.2f}")

    print("\nTax Breakdown:")
    for slab in report["Tax Breakdown"]:
        print(
            f"  Income: ₹{slab['Slab Income']:.2f} | "
            f"Rate: {slab['Rate']} | "
            f"Tax: ₹{slab['Tax']:.2f}"
        )

    print(f"\nRebate (87A)       : ₹{report['Rebate (Section 87A)']:.2f}")
    print(f"Cess (4%)         : ₹{report['Health & Education Cess']:.2f}")
    print(f"Total Tax Payable : ₹{report['Total Tax Payable']:.2f}")
    print(f"Net Annual Salary : ₹{report['Net Annual Salary']:.2f}")
    print("=" * 50)


def main():
    

    print("Welcome to GlobalNext Solutions Tax Calculator\n")

    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")

    try:
        basic = float(input("Enter Monthly Basic Salary: "))
        hra = float(input("Enter Monthly HRA: "))
        allowances = float(input("Enter Monthly Allowances: "))

        report = generate_tax_report(
            emp_id,
            emp_name,
            basic,
            hra,
            allowances
        )

        display_report(report)

    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
