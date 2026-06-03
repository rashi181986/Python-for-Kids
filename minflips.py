def print_min_flips(arr):
    n = len(arr)
    
    # We look for groups that are different from the first element
    for i in range(1, n):
        # Detect the start of a group to flip
        if arr[i] != arr[i - 1]:
            if arr[i] != arr[0]:
                print(f"From {i}", end="")
            # Detect the end of that group
            else:
                print(f" to {i - 1}")
    
    # Handle case where the last group goes to the end of the array
    if arr[n - 1] != arr[0]:
        print(f" to {n - 1}")

# Example:
arr = [0, 1, 1, 0, 0, 0, 1, 1]
print_min_flips(arr)
