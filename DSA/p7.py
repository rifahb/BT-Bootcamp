def get_salary():
    while True:
        try:
            salary=float(input("Enter salary:"))
            return salary
        except ValueError:
            print("Invalid Input! Please enter a valid number.")
name=input("Enter name: ")
salary=get_salary()
if salary>300000:
    print("Salary of",name,"is taxable")
else:
    print("Salary of",name," is not taxable")
