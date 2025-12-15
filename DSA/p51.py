# Coding Challenge 51: Input array

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

print("Array:", arr)
