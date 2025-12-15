N = int(input("Enter N: "))

i = 1
while i*i <= N:
    if i % 4 != 0:       # Skip 4, 8, 12, 16...
        print(i*i, end=" ")
    i += 1
