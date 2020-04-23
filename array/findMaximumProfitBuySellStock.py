# Maximum profit earned by buying and selling shares any number of times
# Given a list containing future prediction of share prices, find maximum profit
# that can be earned by buying and selling shares any number of times with constraint
# that a new transaction can only start after previous transaction is complete.
# i.e. we can only hold at-most one share at a time.
# Stock Prices:  {1, 5, 2, 3, 7, 6, 4, 5}
# Total profit earned is 10
# Buy on day 1 and sell on day 2
# Buy on day 3 and sell on day 5
# Buy on day 7 and sell on day 8
#
# Stock Prices: {10, 8, 6, 5, 4, 2}
# Total profit earned is 0

from typing import List


def findMaximumProfitBuySellStock(arr: List[int]):
    profit = 0
    minIndex = 0
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            minIndex = i

        if (i + 1 == len(arr) or arr[i] > arr[i + 1]) and (arr[i - 1] <= arr[i]):
            profit += arr[i] - arr[minIndex]
            print('Increasing sequences', arr[minIndex: i+1])

    print('Profit:', profit)


array = [1, 5, 2, 3, 7, 6, 4, 5]
array1 = [10, 8, 6, 5, 4, 2]
findMaximumProfitBuySellStock(array)
