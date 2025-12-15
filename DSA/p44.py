# Coding Challenge 44: Reverse of a Number using normal logic

num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10       
    rev = rev * 10 + digit 
    num = num // 10     

print("Reversed Number:", rev)
