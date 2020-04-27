# Longest Increasing Subsequence using Dynamic Programming
# Input 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15
# Longest increasing subsequence is 0, 2, 6, 9, 11, 15
# This subsequence has length 6. In this example, LIS is not unique:
# 0, 4, 6, 9, 11, 15 or
# 0, 4, 6, 9, 13, 15
import sys
from typing import List


def findLISRecursive(arr: List[int], index: int, n: int, prev: int):
    if index == n:
        return 0

    excl = findLISRecursive(arr, index + 1, n, prev)

    incl = 0
    if arr[index] > prev:
        incl = 1 + findLISRecursive(arr, index + 1, n, arr[index])

    return max(excl, incl)


def LISDynamicProgramming(arr: List[int]):
    length = [1] * len(arr)
    subArray = [-1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                if length[j] + 1 >= length[i]:
                    length[i] = length[j] + 1
                    subArray[i] = j

    print('Length array :', length)
    print('Subsequence array:', subArray)
    print('Maximum LIS is', length[-1])

    # print sub sequence
    indexMaxValue = length.index(max(length))
    i = indexMaxValue
    result = []
    result.append(arr[indexMaxValue])
    while subArray[i] != -1:
        result.append(arr[subArray[i]])
        i = subArray[i]

    print(result)


array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
array1 = [0, 4, 12, 2, 10, 6, 9, 13, 3, 11, 7, 15]
#print(findLISRecursive(array, 0, len(array), ~sys.maxsize))
# LISDynamicProgramming(array)
LISDynamicProgramming(array1)

