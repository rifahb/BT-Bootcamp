# Coding Challenge 56: Sum of 2D array

m = int(input("Enter rows: "))
n = int(input("Enter cols: "))

arr = []
total = 0

for i in range(m):
    row = []
    for j in range(n):
        val = int(input(f"Enter element [{i}][{j}]: "))
        row.append(val)
        total += val
    arr.append(row)

print("Sum of all elements:", total)
