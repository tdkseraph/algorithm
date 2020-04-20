# Find index of 0 to be replaced to get maximum length sequence of continuous ones
# Given a binary array, find the index of 0 to be replaced with 1 to get maximum length
# sequence of continuous ones.
# Input { 0, 0, 1, 0, 1, 1, 1, 0, 1, 1 }.
# The index to be replaced is 7 to get continuous sequence of length 6 containing all 1’s

from typing import List


def findIndexLargestSequenceOne(arr: List[int]):
    count = 0
    maxCount = 0
    maxIndex = -1
    prevIndexZero = -1
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            count = i - prevIndexZero
            prevIndexZero = i
        if count > maxCount:
            maxCount = count
            maxIndex = prevIndexZero

    print(maxIndex)


array = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
findIndexLargestSequenceOne(array)