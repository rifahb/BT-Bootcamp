# Coding Challenge 45: Accept n and store elements in array

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

print("Array elements:", arr)
