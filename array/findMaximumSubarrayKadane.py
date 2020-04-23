# Maximum Subarray Problem (Kadane’s algorithm)
# Given an array of integers, find contiguous subarray within it which has the largest sum.
# Input:  {-2, 1, -3, 4, -1, 2, 1, -5, 4}
# Output: Subarray with the largest sum is {4, -1, 2, 1} with sum 6.

from typing import List


def findSubarrayWithLargestNonNegativeSum(arr: List[int]):
    maxEnding = 0
    currentMax = 0
    for i in range(len(arr)):
        maxEnding = maxEnding + arr[i]
        maxEnding = max(maxEnding, 0)
        currentMax = max(maxEnding, currentMax)

    print("The sum of contiguous sub-array with the largest sum (non-negative) is", currentMax)


def findSubarrayWithLargestWithAllNegativeNumber(arr: List[int]):
    maxEnding = arr[0]
    currentMax = arr[0]
    for i in range(len(arr)):
        maxEnding = maxEnding + arr[i]
        maxEnding = max(maxEnding, arr[i])
        currentMax = max(maxEnding, currentMax)

    print("The sum of contiguous sub-array with the largest sum (all negative) is", currentMax)


def findAndPrintSubarrayWithLargestNonNegativeSum(arr: List[int]):
    maxEnding = 0
    currentMax = 0
    begin = 0
    start = 0
    end = 0
    for i in range(len(arr)):
        maxEnding = maxEnding + arr[i]
        if maxEnding < 0:
            begin = i + 1
            maxEnding = 0
        if maxEnding > currentMax:
            start = begin
            end = i
            currentMax = maxEnding

    print("The sum of contiguous sub-array with the largest sum (all negative) is", currentMax)
    print(start, end)
    print(arr[start: end + 1])


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
array1 = [-8, -3, -6, -2, -5, -4]
# findSubarrayWithLargestNonNegativeSum(array)
# findSubarrayWithLargestWithAllNegativeNumber(array1)
findAndPrintSubarrayWithLargestNonNegativeSum(array)
