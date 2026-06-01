def get_rightmost_set_bit(n):
    if n == 0:
        return "No set bits (number is 0)"
    
    # Bitwise trick to isolate the rightmost set bit
    # This works because -n is the 2's complement of n
    rightmost_bit_value = n & -n
    return rightmost_bit_value

# User Input
num = int(input("Enter a number: "))
result = get_rightmost_set_bit(num)

print(f"The value of the rightmost set bit is: {result}")
print(f"Binary representation of input: {bin(num)}")
