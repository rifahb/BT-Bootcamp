# Coding Challenge 48: Maximum value in array

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

max_val = arr[0]
for x in arr:
    if x > max_val:
        max_val = x

print("Maximum value:", max_val)
