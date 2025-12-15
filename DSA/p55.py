# Coding Challenge 55: 2D array row-wise display

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

arr = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    arr.append(row)

print("\nRow-wise display:")
for row in arr:
    print(row)
