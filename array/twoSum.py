# Problem:
# https://leetcode.com/problems/two-sum/submissions/

from typing import List

arr = [2, 7, 11, 7, 15]
sum = 14

arr1 = [3, 2, 4]
sum1 = 6


def twoSum(nums: List[int], target: int) -> List[int]:
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]


def twoSum1(nums: List[int], target: int) -> List[int]:
    s = set()
    for i in range(0, len(nums)):
        temp = target - nums[i]
        if temp in s:
            return [nums.index(temp), i]
        s.add(nums[i])


result = twoSum1(arr, sum)
print(result)
