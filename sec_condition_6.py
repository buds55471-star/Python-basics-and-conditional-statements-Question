# Check whether a number is divisible by both 3 and 5.

n = int(input("Enter a number:"))

if n%3==0 and n%5==0:
    print(f"{n} is divisible by both 3 and 5")
else:
    print(f"{n} is not divisible by both 3 and 5")

