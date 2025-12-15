# Coding Challenge 41: Number to Words

num = input("Enter a number: ")

words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

for digit in num:
    print(words[int(digit)], end=" ")
