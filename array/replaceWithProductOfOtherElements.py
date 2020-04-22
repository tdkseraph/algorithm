# Replace each element of an array with product of every other element without using division operator
# Given an array of integers, replace each element of the array with product of every other element
# in the array without using division operator.
# Input:  { 1, 2, 3, 4, 5 }
# Output: { 120, 60, 40, 30, 24 }
# Input:  { 5, 3, 4, 2, 6, 8 }
# Output: { 1152, 1920, 1440, 2880, 960, 720 }

from typing import List


def replaceElementWithProduct(arr: List[int]):
    leftArr = [1]
    rightArr = [1] * len(arr)
    for i in range(1, len(arr)):
        leftArr.append(leftArr[i - 1] * arr[i - 1])

    for i in range(len(arr) - 2, -1, -1):
        rightArr[i] = rightArr[i + 1] * arr[i + 1]

    for i in range(len(arr)):
        arr[i] = leftArr[i] * rightArr[i]

    print(arr)


array = [1, 2, 3, 4, 5]
array1 = [5, 3, 4, 2, 6, 8]
replaceElementWithProduct(array)