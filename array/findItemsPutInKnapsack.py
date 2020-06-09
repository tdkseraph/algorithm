# 0-1 Knapsack problem
# In 0-1 Knapsack problem, we are given a set of items, each with a weight
# and a value and we need to determine the number of each item to include in
# a collection so that the total weight is less than or equal to a given limit
# and the total value is as large as possible.
# Input:
# value = [ 20, 5, 10, 40, 15, 25 ]
# weight = [ 1, 2, 3, 8, 7, 4 ] W = 10
# Output: Knapsack value is 60
# value = 20 + 40 = 60
# weight = 1 + 8 = 9 < W

from typing import List
import numpy as np


def findItemsPutInKnapsack(valueArr: List[int], weightArr: List[int], target: int):
    memoArr = [[0 for x in range(target + 1)] for x in range(len(valueArr) + 1)]

    for i in range(1, len(valueArr) + 1):
        for j in range(1, target + 1):
            if weightArr[i - 1] > j:
                memoArr[i][j] = memoArr[i - 1][j]
            else:
                currentValue = valueArr[i - 1]
                leftWeight = memoArr[i - 1][j - weightArr[i - 1]]
                previousWeight = memoArr[i - 1][j]
                memoArr[i][j] = max(currentValue + leftWeight, previousWeight)

    print(np.matrix(memoArr))

    # traceback to print selected items
    items = []
    i = len(valueArr)
    j = target

    while i > 0:
        if memoArr[i][j] != memoArr[i - 1][j]:
            items.append(weightArr[i - 1])
            j = j - weightArr[i - 1]

        i -= 1

    print(items)


# value = [20, 5, 10, 40, 15, 25]
# weight = [1, 2, 3, 8, 7, 4]
# W = 10
# findItemsPutInKnapsack(value, weight, W)
value1 = [1, 4, 5, 7]
weight1 = [1, 3, 4, 5]
W1 = 7
findItemsPutInKnapsack(value1, weight1, W1)
