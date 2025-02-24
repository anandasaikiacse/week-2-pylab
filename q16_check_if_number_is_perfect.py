def is_perfect_number(number):
    if number <= 0:
        return False
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum == number

# User input
number = int(input("Enter a number to check if it is perfect: "))

if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")