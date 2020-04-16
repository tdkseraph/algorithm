# Longest sub-array having sum k
# Given an array of integers, find maximum length sub-array having given sum.
# A[] = { 5, 6, -5, 5, 3, 5, 3, -2, 0 }
# Sum = 8
# { -5, 5, 3, 5 } { 3, 5 } { 5, 3 }
# The longest subarray is { -5, 5, 3, 5 } having length 4

from typing import List


def findMaximumLengthSubArray(arr: List[int], target: int):
    maxLen = 0
    sum = 0
    hashmap = {}

    for i in range(len(arr)):
        sum += arr[i]
        if sum == target:
            maxLen = i + 1
        if (sum - target) in hashmap:
            maxLen = max(maxLen, i - hashmap[sum - target])
        if sum not in hashmap:
            hashmap[sum] = i

    print('Length :', maxLen)


def findAndPrintMaximumLengthSubArray(arr: List[int], target: int):
    maxLen = 0
    sum = 0
    fromIndex = 0
    toIndex = 0
    hashmap = {}

    for i in range(len(arr)):
        sum += arr[i]
        if sum == target:
            maxLen = i + 1
        if (sum - target) in hashmap:
            currMaxLen = i - hashmap[sum - target]
            if maxLen <= currMaxLen:
                maxLen = currMaxLen
                fromIndex = hashmap[sum - target] + 1
                toIndex = i + 1
            else:
                toIndex = i + 1
        if sum not in hashmap:
            hashmap[sum] = i

    print('Length :', maxLen)
    print('Sub-array :', arr[fromIndex:toIndex:])


array = [10, 5, 2, 7, 1, 9]
k = 15
# findMaximumLengthSubArray(array, k)
findAndPrintMaximumLengthSubArray(array, k)