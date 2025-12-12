def get_and_validate(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

P=get_and_validate("Enter Principal amount:")
T=get_and_validate("Enter Time Period(in years): ")
R=get_and_validate("Enter Rate of Interest: ")
SI=(P*T*R)/100
print("Interest amount: ",SI)