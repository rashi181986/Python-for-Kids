def find_missing(arr):
    # n is the length of the array plus the one missing number
    n = len(arr) + 1
    
    # Calculate what the sum should be
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the numbers we have
    actual_sum = sum(arr)
    
    # The difference is the missing number
    return expected_sum - actual_sum

# Example:
arr = [1, 4, 3, 2, 6]
print(f"The missing number is: {find_missing(arr)}")
