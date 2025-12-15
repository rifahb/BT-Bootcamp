# Coding Challenge 49: Search element in array

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

target = int(input("Enter element to search: "))

found = False
for x in arr:
    if x == target:
        found = True
        break

if found:
    print("Element found!")
else:
    print("Element NOT found.")
