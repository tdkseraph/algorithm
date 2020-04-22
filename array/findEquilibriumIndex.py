# Find Equilibrium Index of an Array
# Given an array of integers, find equilibrium index in it.
# (A[0] + A[1] + ... + A[i-1]) = (A[i+1] + A[i+2] + ... + A[n-1])   where 0 < i < n-1
#  {0, -3, 5, -4, -2, 3, 1, 0}
#  The equilibrium index found at index 0, 3 and 7

from typing import List


def findEquilibriumIndex(arr: List[int]):
    sumArr = sum(arr)
    sumRight = 0
    for i in range(len(arr)):
        if sumArr - arr[i] - sumRight == sumRight:
            print('Equilibrium Index found at', i)
        sumRight += arr[i]

array = [0, -3, 5, -4, -2, 3, 1, 0]
findEquilibriumIndex(array)