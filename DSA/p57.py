# Coding Challenge 57: Search element in 2D array

m = int(input("Enter rows: "))
n = int(input("Enter cols: "))

arr = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    arr.append(row)

key = int(input("Enter element to search: "))

found = False

for i in range(m):
    for j in range(n):
        if arr[i][j] == key:
            print(f"Element found at position [{i}][{j}]")
            found = True

if not found:
    print("Element not found.")
