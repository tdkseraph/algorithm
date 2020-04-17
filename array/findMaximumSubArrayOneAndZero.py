# Find maximum length sub-array having equal number of 0’s and 1’s
# Given a binary array containing 0 and 1, find maximum length sub-array having equal number of 0’s and 1’s.
# Input: {0, 0, 1, 0, 1, 0, 0}
# Output: {0, 1, 0, 1} or {1, 0, 1, 0}

from typing import List


def findMaximumSubArrayOneAndZero(arr: List[int]):
    maxLen = 0
    sum = 0
    hashmap = {}
    for i in range(len(arr)):
        if (arr[i] == 0):
            sum += -1
        else:
            sum += 1

        if sum in hashmap:
            print(arr[hashmap[sum]:i])  # print sub-array
            maxLen = max(maxLen, i - hashmap[sum])
        else:
            hashmap[sum] = i

    print('Hashmap: ', hashmap)
    print('Maximum: ', maxLen)
    print('From: ', maxLen)


array = [0, 0, 1, 0, 1, 0, 0]
findMaximumSubArrayOneAndZero(array)
