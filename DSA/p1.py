try:
        num1 = float(input("Enter first number: "))
except ValueError:
        print("Invalid input!")
try:
        num2 = float(input("Enter second number: "))
except ValueError:
        print("Invalid input!")
sum_val = num1 + num2
avg = sum_val / 2

print("Sum of numbers:", sum_val)
print("Average of numbers:", avg)