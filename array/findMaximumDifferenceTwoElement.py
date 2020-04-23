# Find maximum difference between two elements in an array by satisfying given constraints
# Given an array of integers, find the maximum difference between two elements in the
# array such that smaller element appears before the larger element.
# Input:  { 2, 7, 9, 5, 1, 3, 5 }
# Output: The maximum difference is 7

from typing import List
import sys


def findMaximumDifference(arr: List[int]):
    min = sys.maxsize
    diff = 0
    for i in range(0, len(arr)):
        if arr[i] > min and diff < arr[i] - min:
            diff = arr[i] - min
        elif arr[i] <= min:
            min = arr[i]

    print(diff)


array = [2, 7, 9, 5, 1, 3, 10]
array1 = [2, 7, 9, 5, 1, 3, 5]
findMaximumDifference(array1)
findMaximumDifference(array)
