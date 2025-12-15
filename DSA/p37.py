# Coding Challenge 37: Increasing Number Pattern

N = int(input("Enter N: "))

for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
