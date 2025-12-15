# Coding Challenge 50: Count odd and even numbers

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

odd = 0
even = 0

for x in arr:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of even elements:", even)
print("Number of odd elements :", odd)
