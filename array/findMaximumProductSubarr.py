# Find maximum product subarray in a given array
# Given an array of integers, find maximum product subarray.
# In other words, find a sub-array that has maximum product of its elements.
# Input:  { -6, 4, -5, 8, -10, 0, 8 }
# Output: The maximum product sub-array is {4, -5, 8, -10} having product 1600
# Input:  { 40, 0, -20, -10 }
# Output: The maximum product sub-array is {-20, -10} having product 200

from typing import List


def findMaximumProductSubArr(arr: List[int]):
    maxEnding = 0
    minEnding = 0
    maxCurrent = 0

    for i in range(len(arr)):
        tmp = maxEnding
        maxEnding = max(arr[i], max(arr[i]*maxEnding, arr[i]*minEnding))
        minEnding = min(arr[i], min(arr[i]*tmp, arr[i]*minEnding))
        maxCurrent = max(maxEnding, maxCurrent)

    print('The maximum product of a sub-array is', maxCurrent)


array = [-6, 4, -5, 8, -10, 0, 8]
array1 = [40, 0, -20, -10]
array2 = [-6, 0, 0]
array3 = [0, 0, 0]
findMaximumProductSubArr(array)
