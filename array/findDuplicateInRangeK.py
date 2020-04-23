# Find duplicates within given range k in an array.
# Given an array and a positive number k, check whether the array contains any duplicate
# elements within range k. If k is more than size of the array, the solution should check
# for duplicates in the complete array.
# A[] = { 5, 6, 8, 2, 4, 6, 9 } k = 4
# Output: Duplicates found (element 6 is repeated at distance 4 which is <= k)

# A[] = { 5, 6, 8, 2, 4, 6, 9 } k = 2
# Output: No Duplicates found (element 6 is repeated at distance 4 which is > k)

# A[] = { 1, 2, 3, 2, 1 } k = 7
# Output: Duplicates found (element 1 and 2 is repeated at distance 4 and 2 respectively which are both <= k)

from typing import List


def findDuplicateInRangeK(arr: List[int], k: int):
    hashset = set()
    for i in range(len(arr)):
        if arr[i] in hashset:
            print('Duplicates found at index', i, 'with value', arr[i])
            return

        hashset.add(arr[i])

        if i >= k:
            hashset.remove(arr[i - k])

    print('No duplicated item found')


array = [5, 6, 8, 2, 4, 6, 9]
findDuplicateInRangeK(array, 4)
# findDuplicateInRangeK(array, 2)
#
# array1 = [1, 2, 3, 2, 1]
# findDuplicateInRangeK(array1, 7)
