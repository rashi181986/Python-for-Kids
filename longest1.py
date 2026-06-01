def longest_consecutive_ones(n):
    count = 0
    while n > 0:
        # Bitwise AND with its own left-shifted version
        # This effectively removes one '1' from every cluster of 1s
        n = n & (n << 1)
        count += 1
    return count

# User Input
num = int(input("Enter a number: "))

result = longest_consecutive_ones(num)

print(f"Binary representation: {bin(num)[2:]}")
print(f"Longest consecutive 1s: {result}")
