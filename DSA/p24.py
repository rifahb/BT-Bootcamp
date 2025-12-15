# Coding Challenge 24: Fibonacci series up to N

N = int(input("Enter N: "))

a, b = 1, 1

while a <= N:
    print(a, end=" ")
    a, b = b, a + b
