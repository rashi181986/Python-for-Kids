def longest_alternating_subarray(arr):
    if not arr:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(arr)):
        # Check if the current and previous elements have different parity
        # (Even-Odd or Odd-Even)
        if (arr[i] % 2 == 0 and arr[i-1] % 2 != 0) or \
           (arr[i] % 2 != 0 and arr[i-1] % 2 == 0):
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            # Reset current length if the pattern breaks
            current_len = 1
            
    return max_len

# Example:
a = [6, 4, 9, 4, 7, 2, 3, 4, 2, 52]
print(f"Length of longest alternating subarray: {longest_alternating_subarray(a)}")
