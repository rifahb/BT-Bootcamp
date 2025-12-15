N = int(input("Enter value of N: "))

print("Series:")
term = 1
increment = 1

while term <= N:
    print(term, end=" ")
    increment += 1
    term += increment
