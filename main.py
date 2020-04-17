# Sort an array containing 0’s, 1’s and 2’s (Dutch national flag problem)
# Given an array containing only 0’s, 1’s and 2’s, sort the array in linear time and using constant space.
# Input:  { 0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0 }
# Output: { 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2 }

from typing import List


def sortArrayZeroOneTwo(arr : List[int]):
    start = 0
    mid = 0
    end = len(arr) - 1
    pivot = 1
    while mid <= end:
        if arr[mid] < pivot:
            swap(arr, start, mid)
            start += 1
            mid += 1
        elif arr[mid] > pivot:
            swap(arr, mid, end)
            end -= 1
        else:
            mid += 1

    print(arr)


def swap(arr: List[int], i: int, j: int):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


array = [ 0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
sortArrayZeroOneTwo(array)