# In-place merge two sorted arrays
# Given two sorted arrays X[] and Y[] of size m and n each, merge elements
# of X[] with elements of array Y[] by maintaining the sorted order.
# i.e. fill X[] with first m smallest elements and fill Y[] with remaining elements.
# Input:
# X[] = { 1, 4, 7, 8, 10 }
# Y[] = { 2, 3, 9 }
#
# Output:
# X[] = { 1, 2, 3, 4, 7 }
# Y[] = { 8, 9, 10 }

import math
from typing import List

# O(m*n)
def mergeTwoSortedArray(xArr: List[int], yArr: List[int]):
    xIndex = 0
    yIndex = 0
    for i in range(len(xArr)):
        if xArr[xIndex] > yArr[yIndex]:
            tmp = xArr[xIndex]
            xArr[xIndex] = yArr[yIndex]
            yArr[yIndex] = tmp
            xIndex += 1
            # sort yArray by correct order
            for j in range(1, len(yArr)):
                if yArr[j - 1] >= yArr[j]:
                    tmp = yArr[j]
                    yArr[j] = yArr[j - 1]
                    yArr[j - 1] = tmp

        elif xArr[xIndex] < yArr[yIndex]:
            xIndex += 1

    print(xArr)
    print(yArr)


def nextGap(gap: int):
    if gap <= 1:
        return 0
    return math.floor(gap/2)

# O((n+m)*log(n+m)) time with O(1) extra space
# https://www.geeksforgeeks.org/efficiently-merging-two-sorted-arrays-with-o1-extra-space/
def mergeTwoSortedArrayByShellSort(xArr: List[int], yArr: List[int]):
    n = len(xArr)
    m = len(yArr)
    gap = nextGap(n+m)
    while gap > 0:
        index = 0
        while index + gap < n:
            if xArr[index] > xArr[index + gap]:
                xArr[index], xArr[index + gap] = xArr[index + gap], xArr[index]
            index += 1

        while index < n <= index + gap < n + m:
            if xArr[index] > yArr[index + gap - n]:
                xArr[index], yArr[index + gap - n] = yArr[index + gap - n], xArr[index]
            index += 1

        while index >= n and index + gap < n + m:
            if yArr[index - n] > yArr[index - n + gap]:
                yArr[index - n], yArr[index - n + gap] = yArr[index - n + gap], yArr[index - n]
            index += 1

        gap = nextGap(gap)

    print(xArr)
    print(yArr)


xArray = [1, 4, 7, 8, 10]
yArray = [2, 3, 9]

xArray1 = [10]
yArray1 = [2, 3]

xArray2 = [1, 5, 9, 10, 15, 20]
yArray2 = [2, 3, 8, 13]

# mergeTwoSortedArray(xArray, yArray)
mergeTwoSortedArrayByShellSort(xArray, yArray)
