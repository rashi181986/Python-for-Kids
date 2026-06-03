def sum_numbers(n):
    # Base case
    if n == 0:
        return 0

    # Recursive case
    return n + sum_numbers(n - 1)

# Input from user
n = int(input("Enter a number: "))

# Function call and output
result = sum_numbers(n)
print("Sum =", result)