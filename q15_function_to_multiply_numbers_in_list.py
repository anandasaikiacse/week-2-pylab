def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage:
numbers = [2, 3, 4]
print("The numbers in the list are:", numbers)
print("The product is:", multiply_numbers(numbers))