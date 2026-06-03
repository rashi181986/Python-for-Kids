def sort_012(a):
    low = 0
    mid = 0
    high = len(a) - 1

    while mid <= high:
        if a[mid] == 0:
            # Swap 0 to the front
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            # 1 is in the right place, just move forward
            mid += 1
        else: # a[mid] == 2
            # Swap 2 to the back
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a

# Example usage:
a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print(*(sort_012(a)))
