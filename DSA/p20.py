N = int(input("Enter value of N: "))

print("Series:")
for n in range(1, N + 1):
    if n % 4 != 0:       # skip multiples of 4
        print(n * n, end=" ")
