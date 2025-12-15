# Program to check if a number is even or odd with error handling

def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

num = get_integer("Enter a number: ")

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
