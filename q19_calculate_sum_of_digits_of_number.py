def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))  # Convert number to string, iterate, and sum the digits

# User input
num = int(input("Enter a number: "))

# Output the result
print(f"The sum of the digits of {num} is {sum_of_digits(num)}.")