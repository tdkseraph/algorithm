# Find minimum sum subarray of given size k
# Given an array of integers, find minimum sum sub-array of given size k.
# Input:  {10, 4, 2, 5, 6, 3, 8, 1}, k = 3
# Output: Minimum sum sub-array of size 3 is (1, 3)

import sys
from typing import List


def findMinimumSubArraySizeK(arr: List[int], k: int):
    currentMin = sys.maxsize
    sumWindow = 0
    start = 0
    end = 0

    for i in range(len(arr)):
        sumWindow += arr[i]

        if i + 1 >= k:
            if currentMin > sumWindow:
                currentMin = sumWindow
                start = i + 1 - k
                end = i

            sumWindow -= arr[i + 1 - k]

    print('Minimum sum sub-array has value', currentMin, ' is from', start, 'to', end)
    print(arr[start:end + 1])


array = [10, 4, 2, 5, 6, 3, 8, 1]
findMinimumSubArraySizeK(array, 3)
