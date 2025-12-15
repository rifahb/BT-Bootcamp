# Coding Challenge 40: Factorial Pattern

import math

N = int(input("Enter N: "))
num = 1

for i in range(1, N + 1):
    for _ in range(i):
        print(math.factorial(num), end=" ")
        num += 1
    print()
