import numpy as np

# 1. Creating an array
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print("-" * 30)

# 2. Basic Mathematical Operations (Element-wise)
print("Arithmetic Operations:")
print(f"Addition (arr1 + arr2):       {arr1 + arr2}")
print(f"Subtraction (arr1 - arr2):    {arr1 - arr2}")
print(f"Multiplication (arr1 * arr2): {arr1 * arr2}")
print(f"Division (arr1 / arr2):       {arr1 / arr2}")
print("-" * 30)

# 3. Statistical Operations
print("Statistical Operations:")
print(f"Mean of arr1:    {np.mean(arr1)}")
print(f"Maximum value:   {np.max(arr1)}")
print(f"Minimum value:   {np.min(arr1)}")
print(f"Sum of elements: {np.sum(arr1)}")
print("-" * 30)

# 4. Reshaping Arrays
# Creating a 1D array of 6 elements and reshaping it into a 2x3 matrix
arr_3d = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr_3d.reshape(2, 3)
print("Reshaped Array (2x3 Matrix):")
print(reshaped)
print("-" * 30)

# 5. Slicing and Indexing
print(f"First element:        {arr1[0]}")
print(f"Elements from index 1 to 3: {arr1[1:4]}")
