# Coding Challenge 46: Sum of array elements

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

total = sum(arr)

print("Sum of all elements:", total)
