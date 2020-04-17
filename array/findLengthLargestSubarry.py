# Length of the largest subarray with contiguous elements
# Given an array of distinct integers, find length of the longest
# subarray which contains numbers that can be arranged in a continuous sequence.
#
# Input:  arr[] = {10, 12, 11};
# Output: Length of the longest contiguous subarray is 3
#
# Input:  arr[] = {14, 12, 11, 20};
# Output: Length of the longest contiguous subarray is 2
#
# Input:  arr[] = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45};
# Output: Length of the longest contiguous subarray is 5
from typing import List


def findLengthLargestSubarray(arr : List[int]):
    maxLen = 0
    for i in range(len(arr)):
        max = arr[i]
        min = arr[i]

        for j in range(i+1, len(arr)):
                if max <= arr[j]: max = arr[j]
                if min >= arr[j]: min = arr[j]
                if (max - min == j - i) and (maxLen < max - min + 1):
                    maxLen = max - min + 1

    print(maxLen)


array1 = [10, 12, 11]
array2 = [14, 12, 11, 20]
array3 = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
findLengthLargestSubarray(array3)











