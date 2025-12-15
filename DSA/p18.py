while True:
    try:
        N = int(input("Enter value of N: "))
        if N >= 2:
            break
        else:
            print("N must be at least 2.\n")
    except:
        print("Please enter a valid integer.\n")

print("Series:")
for i in range(2, N + 1, 2):   # even numbers only
    print(i * i, end=" ")
