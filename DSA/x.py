number=5
a, b=0,1
n=int(input("Enter number of terms: "))
for i in range(n):
    number+=a
    a, b=b, a+b
    print(number, end=" ")