# Length of longest continuous sequence with same sum in given binary arrays
# For example, consider below binary arrays X[] and Y[]
#   X: {0, 0, 1, 1, 1, 1}
#   Y: {0, 1, 1, 0, 1, 0}
# The length of longest continuous sequence with same sum is 5 as
#   X[0, 4]: {0, 0, 1, 1, 1}      (sum = 3)
#   Y[0, 4]: {0, 1, 1, 0, 1}      (sum = 3)

from typing import List


def findLongestSequenceSameSumInTwoArray(arrX: List[int], arrY: List[int]):
    sumX = 0
    sumY = 0
    diff = 0
    result = 0
    hashtable = {0: -1}

    for i in range(len(arrX)):
        sumX += arrX[i]
        sumY += arrY[i]
        diff = sumX - sumY

        if diff in hashtable:
            result = max(result, i - hashtable[diff])
        else:
            hashtable[diff] = i

    print(hashtable)
    print('The length of longest continuous sequence with same sum is', result)


arrayX = [0, 0, 1, 1, 1, 1]
arrayY = [0, 1, 1, 0, 1, 0]
findLongestSequenceSameSumInTwoArray(arrayX, arrayY)
