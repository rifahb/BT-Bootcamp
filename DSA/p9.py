def get_year():
    while True:
        try:
            year = int(input("Enter a year: "))
            return year
        except ValueError:
            print("Invalid Input! Please enter a valid year.")
year = get_year()
if year%4==0 and (year%100!=0 or year%400==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")