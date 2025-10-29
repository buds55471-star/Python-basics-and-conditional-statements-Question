# Check if a number is a palindrome.

n = input("Enter a number:")
new = n[::-1]

if n == new:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

