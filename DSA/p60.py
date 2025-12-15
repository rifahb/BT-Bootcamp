# Coding Challenge 60: Matrix multiplication

# First matrix
r1 = int(input("Enter rows of Matrix 1: "))
c1 = int(input("Enter cols of Matrix 1: "))

A = []
print("Enter Matrix 1:")
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)

# Second matrix
r2 = int(input("Enter rows of Matrix 2: "))
c2 = int(input("Enter cols of Matrix 2: "))

# Check multiplication rule
if c1 != r2:
    print("Matrix multiplication NOT possible!")
    exit()

B = []
print("Enter Matrix 2:")
for i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input(f"B[{i}][{j}]: ")))
    B.append(row)

# Create result matrix
C = [[0] * c2 for _ in range(r1)]

# Multiply
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            C[i][j] += A[i][k] * B[k][j]

print("\nResultant Matrix (A x B):")
for row in C:
    print(row)
