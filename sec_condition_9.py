# Check if a number is an Armstrong number.

number = int(input("Enter a number: "))

# Find the number of digits
num_digits = len(str(number))

# Compute the sum of digits raised to the power of num_digits
sum_of_powers = 0
temp = number

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

# Conditional check
if number == sum_of_powers:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

