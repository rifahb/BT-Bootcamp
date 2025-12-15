# Coding Challenge 38: Fibonacci Series Pattern

N = int(input("Enter N: "))

a, b = 1, 1

for i in range(1, N + 1):
    for _ in range(i):
        print(a, end=" ")
        a, b = b, a + b
    print()
