# Coding Challenge 39: Perfect Squares with Alternating Signs

N = int(input("Enter N: "))

num = 1
for i in range(1, N + 1):
    for _ in range(i):
        sq = num * num
        if num % 2 == 0:
            sq = -sq
        print(sq, end=" ")
        num += 1
    print()
