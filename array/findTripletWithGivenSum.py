# Find Triplet with given sum in an array
# Given an unsorted array of integers, find a triplet with given sum in it.
# Input: arr = [ 2, 7, 4, 0, 9, 5, 1, 3 ] sum = 6
# Output: Triplet exists.
# (0 1 5), (0 2 4), (1 2 3)

from typing import List


def findTripletWithGivenSum(arr: List[int], targetSum: int):
    hashtable = {}
    checkArr = {}

    for i in range(len(arr)):
        hashtable[arr[i]] = i

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            remain = targetSum - (arr[i] + arr[j])
            if remain in hashtable:
                check = 0
                if checkArr.get(remain):
                    check += 1
                if checkArr.get(arr[j]):
                    check += 1
                if checkArr.get(arr[i]):
                    check += 1

                if check < 3:
                    print(remain, arr[j], arr[i])
                    checkArr[arr[j]] = True
                    checkArr[remain] = True
                    checkArr[arr[i]] = True


array = [2, 7, 4, 0, 9, 5, 1, 3]
targetSum = 6
findTripletWithGivenSum(array, targetSum)
