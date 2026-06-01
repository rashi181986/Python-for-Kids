# Input binary string from the user
binary_string = input("Enter a binary number: ")

try:
    # Convert binary string to base-10 decimal integer
    decimal_value = int(binary_string, 2)
    print(f"The decimal value is: {decimal_value}")
except ValueError:
    print("Invalid binary number! Please enter only 0s and 1s.")
