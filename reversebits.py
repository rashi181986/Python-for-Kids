def reverse_bits(n, bit_size=8):
    result = 0
    for i in range(bit_size):
        # Shift result left to make room for the next bit
        result <<= 1
        # Extract the rightmost bit of n and add it to result
        result |= (n & 1)
        # Shift n right to process the next bit
        n >>= 1
    return result

# User Input
num = int(input("Enter a number: "))
bits = int(input("Enter bit-size (e.g., 8, 16): "))

new_number = reverse_bits(num, bits)

print(f"Original Binary: {bin(num)[2:].zfill(bits)}")
print(f"Reversed Binary: {bin(new_number)[2:].zfill(bits)}")
print(f"Newly formed decimal number: {new_number}")
