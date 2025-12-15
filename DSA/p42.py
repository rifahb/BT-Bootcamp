# Coding Challenge 42: Alternating +4, -4 Series

N = int(input("Enter N: "))

num = 1
sign = -1

while abs(num) <= N:
    print(num, end=" ")
    num += 4 * sign
    sign *= -1
