a = [4, 5, 234, 2, 6, 82, 234, 5234]

def find_max_diff(arr):
    if not arr:
        return 0
    
    # The max difference is always Max Value - Min Value
    return max(arr) - min(arr)

print("Maximum difference:", find_max_diff(a))
