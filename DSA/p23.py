# Coding Challenge 23: Display the series 1,5,9,13,21,25,29,37,41...N

N = int(input("Enter N: "))

num = 1
toggle = True  # True → add 4, False → add 8

while num <= N:
    print(num, end=" ")
    if toggle:
        num += 4
    else:
        num += 8
    toggle = not toggle
