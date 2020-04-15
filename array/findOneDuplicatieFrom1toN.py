# Find duplicate element in a limited range array
# Given a limited range array of size n where array contains
# elements between 1 to n-1 with one element repeating, find the duplicate number in it.
# Input:   { 1, 2, 3, 4, 4 }
# Input:   { 1, 2, 3, 4, 2 }

from typing import List


def findDuplicate(arr: List[int]):
    negativeSum = 0
    positiveSum = 0
    for i in range(len(arr)):
        positiveSum += arr[i]
        negativeSum -= i

    print(positiveSum + negativeSum)

def findDuplicate1(arr: List[int]):
    xor = 0
    for i in range(len(arr)):
        xor ^= arr[i]
        xor ^= i

    print(xor)


array = [1, 2, 3, 4, 2]
array1 = [1, 2, 3, 4, 4]

findDuplicate1(array)
