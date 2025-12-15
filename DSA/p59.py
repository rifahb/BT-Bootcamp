# Coding Challenge 58: Matrix and transpose

m = int(input("Enter rows: "))
n = int(input("Enter cols: "))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    matrix.append(row)

print("\nMatrix:")
for row in matrix:
    print(row)

print("\nTranspose:")
for j in range(n):
    for i in range(m):
        print(matrix[i][j], end=" ")
    print()
