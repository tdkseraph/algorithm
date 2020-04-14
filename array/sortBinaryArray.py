# Sort Binary Array in Linear Time
# Given a binary array, sort it in linear time and constant space.
# Output should print contain all zeroes followed by all ones.
# Input: { 1, 0, 1, 0, 1, 0, 0, 1 }
# Output:{ 0, 0, 0, 0, 1, 1, 1, 1 }


from typing import List


def sort(arr: List[int]):
    pivot = 1
    j = 0

    for i in range(len(arr)):
        if arr[i] < pivot:
            swap(arr, i, j)
            j += 1


def swap(arr: List[int], i: int, j: int):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


array = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
sort(array)
print(array)
