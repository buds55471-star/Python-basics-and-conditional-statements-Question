# Check if a year is a leap year (using nested if).

year = int(input("Enter a year:"))

if year%4 or year%400==0:
    if year%100!=0:
        print(f"{year} is a leap year")

