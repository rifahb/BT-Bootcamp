while True:
    try:
        N = int(input("Enter value of N: "))
        if N > 0:
            break
        else:
            print("N must be a positive number.\n")
    except:
        print("Please enter a valid integer.\n")

print("Series:")
for i in range(1, N + 1):
    print(i, end=" ")
