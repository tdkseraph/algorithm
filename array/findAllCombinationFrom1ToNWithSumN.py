# Print all combination of numbers from 1 to n having sum n
# Given a positive integer n, print all combination of numbers from 1 to n having sum n
# For n = 5, below combinations are possible
# { 5 }
# { 1, 4 }
# { 2, 3 }
# { 1, 1, 3 }
# { 1, 2, 2 }
# { 1, 1, 1, 2 }
# { 1, 1, 1, 1, 1 }

from typing import List


def printAllCombinations(n, s, start):
    if n == 0:
        print(s)
    for i in range(start, n + 1):
        printAllCombinations(n - i, s + ' ' + str(i), i)


def findAllCombinationFrom1ToNWithSumN(i: int, n: int, result: List[int], index: int):
    if n == 0:
        print(result[0: index])

    j = i
    for j in range(j, n + 1):
        result[index] = j
        print('j=', j, 'n=', n, 'n-j=', n - j, 'index=', index + 1, 'result=', result)
        findAllCombinationFrom1ToNWithSumN(j, n - j, result, index + 1)


n = 3
array = [0] * n
findAllCombinationFrom1ToNWithSumN(1, n, array, 0)
# printAllCombinations(n, '', 1)
