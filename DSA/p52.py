# Coding Challenge 52: Reverse array

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

rev = arr[::-1]
print("Reversed Array:", rev)
