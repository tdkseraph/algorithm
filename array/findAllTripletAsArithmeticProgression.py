# Print all Triplets that forms Arithmetic Progression
# Given a sorted array of distinct positive integers, print all triplets that
# forms Arithmetic Progression with integral common difference.
# Input: A[] = { 5, 8, 9, 11, 12, 15 }
# Output: { 5 8 11 } { 9 12 15}
# Input: A[] = { 1, 3, 5, 6, 8, 9, 15 }
# Output: {1 3 5} {1 5 9} {3 6 9} {1 8 15} {3 9 15}

from typing import List


def findAllTripletAsArithmeticProgression(arr: List[int]):
    hashmap = {}
    for i in range(len(arr)):
        hashmap[arr[i]] = arr[i]

    for i in range(1, len(arr) - 1):
        for j in range(0, i):
            if arr[i] + (arr[i] - arr[j]) in hashmap:
                print('Found ', arr[j], arr[i], arr[i] + (arr[i] - arr[j]))


array = [5, 8, 9, 11, 12, 15]
array1 = [1, 3, 5, 6, 8, 9, 15]
findAllTripletAsArithmeticProgression(array1)
