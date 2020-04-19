# Quicksort
# https://www.youtube.com/watch?v=ZHVk2blR45Q
# This function takes last element as pivot.

from typing import List


def quickSort(arr: List[int], left: int, right: int):
    if left < right:
        mid = partition(arr, left, right)
        quickSort(arr, left, mid - 1)
        quickSort(arr, mid + 1, right)


def partition(arr: List[int], left: int, right: int) -> int:
    pivot = arr[right]
    counter = left - 1
    for i in range(left, right):
        if arr[i] < pivot:
            counter += 1
            arr[i], arr[counter] = arr[counter], arr[i]

    arr[counter+1], arr[right] = arr[right], arr[counter+1]
    return counter + 1


array = [10, 30, 40, 50, 70, 90, 80]
array1 = [10, 7, 12, 8, 3, 2, 6]
quickSort(array1, 0, len(array1) - 1)
print(array1)