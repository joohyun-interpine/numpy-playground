# Example 1: Logical AND between two boolean arrays
import numpy as np

arr1 = np.array([True, False, True, False])
arr2 = np.array([True, True, False, True])
result = np.logical_and(arr1, arr2)
print("Example 1: Logical AND between two boolean arrays", result)
# Output: [True False False False]

# Example 2: Logical AND between two numeric arrays

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([0, 1, 0, 3])
result = np.logical_and(arr1, arr2)
print("Logical AND between two numeric arrays", result)
# Output: [False True False True]

# Example 3: Logical AND with a condition

arr = np.array([1, 2, 3, 4])
cond = np.array([True, False, True, False])
result = np.logical_and(arr > 2, cond)
print("Logical AND with a condition", result)
# Output: [False False True False]