# Sort an array in one swap whose two elements are swapped by mistake
# Given an array where all its elements are sorted except two elements which
# were swapped, sort the array in linear time. Assume there are no duplicates in the array.
# Input:  A[] = [3, 8, 6, 7, 5, 9] OR [3, 5, 6, 9, 8, 7] OR [3, 5, 7, 6, 8, 9]
# Output: A[] = [3, 5, 6, 7, 8, 9]

from typing import List


def sortArrayByOneSwap(arr: List[int]):
    x = -1
    y = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
           if x == -1 and y == -1:
                x = i - 1
                y = i
           else:
                y = i

    arr[x], arr[y] = arr[y], arr[x]
    print('After :', arr)


array = [3, 8, 6, 7, 5, 9]
sortArrayByOneSwap(array)