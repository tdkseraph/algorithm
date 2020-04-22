# Find maximum difference between two elements in an array by satisfying given constraints
# Given an array of integers, find the maximum difference between two elements in the
# array such that smaller element appears before the larger element.
# Input:  { 2, 7, 9, 5, 1, 3, 5 }
# Output: The maximum difference is 7

from typing import List


def findMaximumDifference(arr: List[int]):
    min = arr[0]
    diff = 0
    for i in range(1, len(arr)):
        if arr[i] >= min and arr[i] - min >= diff:
            diff = arr[i] - min
        # else:
    print(diff)


array = [2, 7, 9, 5, 1, 3, 5]
findMaximumDifference(array)
