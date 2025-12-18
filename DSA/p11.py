def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Enter a number.")


def calculate_gross_monthly(basic, allowance):
    return basic + allowance


def calculate_annual_gross(gross_monthly, bonus_percent):
    annual_salary = gross_monthly * 12
    bonus_amount = (annual_salary * bonus_percent) / 100
    return annual_salary + bonus_amount


def main():
    print("=== Employee Salary Calculator ===")

    
    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")

    basic_salary = get_positive_float("Enter Basic Monthly Salary: ₹")
    special_allowance = get_positive_float("Enter Special Allowances (Monthly): ₹")
    bonus_percent = get_positive_float("Enter Annual Bonus (% of Annual Gross Salary): ")

   
    gross_monthly = calculate_gross_monthly(basic_salary, special_allowance)
    annual_gross = calculate_annual_gross(gross_monthly, bonus_percent)

    
    print("\n======= EMPLOYEE SALARY REPORT =======")
    print(f"Employee Name        : {name}")
    print(f"Employee ID          : {emp_id}")
    print(f"Gross Monthly Salary : ₹{gross_monthly:,.2f}")
    print(f"Annual Gross Salary  : ₹{annual_gross:,.2f}")
    print("=======================================")

main()
