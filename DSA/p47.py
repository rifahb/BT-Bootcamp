# Coding Challenge 47: Minimum value in array

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

min_val = arr[0]
for x in arr:
    if x < min_val:
        min_val = x

print("Minimum value:", min_val)
