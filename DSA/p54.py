# Coding Challenge 54: Binary Search

n = int(input("Enter number of elements: "))
arr = []

print("Enter elements in sorted order:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

key = int(input("Enter element to search: "))

low, high = 0, n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        found = True
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found:
    print("Element found at index:", mid)
else:
    print("Element not found.")
