# Coding Challenge 53: Sort array ascending/descending

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

choice = input("Sort Ascending (A) or Descending (D)? ").lower()

if choice == "a":
    arr.sort()
elif choice == "d":
    arr.sort(reverse=True)
else:
    print("Invalid choice")

print("Sorted Array:", arr)
