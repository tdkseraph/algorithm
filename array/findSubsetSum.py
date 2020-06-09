# Given a set of positive integers and an integer s, is there any non-empty subset whose sum to s.
# Input: array = [1, 2, 5, 7] and sum = 8
# Output: Yes
# (5, 2, 1)

from typing import List
import numpy as np


def findSubsetSum(arr: List[int], targetSum: int):
    memoArr = [[0 for x in range(targetSum + 1)] for x in range(len(arr) + 1)]

    for i in range(0, len(arr) + 1):
        memoArr[i][0] = True

    for i in range(1, len(arr) + 1):
        memoArr[0][i] = False

    for i in range(1, len(arr) + 1):
        for j in range(0, targetSum + 1):
            if arr[i - 1] > j:
                memoArr[i][j] = memoArr[i - 1][j]
            else:
                include = memoArr[i - 1][j - arr[i - 1]]
                exclude = memoArr[i - 1][j]
                memoArr[i][j] = include or exclude

    print(np.matrix(memoArr))

    #backtracking
    items = []
    i = len(arr)
    j = targetSum
    while i > 0:
        if memoArr[i][j] != memoArr[i - 1][j]:
            items.append(arr[i-1])
            j = j - arr[i - 1]
        i -= 1

    print(items)


array = [1, 2, 5, 7]
sum = 8
findSubsetSum(array, sum)

#   0 1 2 3 4 5 6 7 8
# 0 T F F F F F F F F
# 1 T T F F F F F F F
# 2 T T T T F F F F F
# 5 T T T T F T T T T
# 7 T T T T F T T T T
