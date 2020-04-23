# Find the maximum sequence of continuous 1’s that can be formed by replacing at-most k zeroes by ones
# { 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0 }
# For k = 0, The length of longest sequence is 4 (from index 6 to 9)
# For k = 1, The length of longest sequence is 7 (from index 3 to 9)
# For k = 2, The length of longest sequence is 10 (from index 0 to 9)

from typing import List


def maximumSeqOneByReplaceKZero(arr: List[int], k: int):
    zeroCounter = 0
    startIndexWindow = 0
    currentMaxWindow = 0
    startMaxWindow = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            zeroCounter += 1

        while zeroCounter > k:
            if arr[startIndexWindow] == 0:
                zeroCounter -= 1

            startIndexWindow += 1

        if i - startIndexWindow + 1 > currentMaxWindow:
            currentMaxWindow = i - startIndexWindow + 1
            startMaxWindow = startIndexWindow

    print("The longest sequence has length", currentMaxWindow, " from index",
          startMaxWindow, " to", (currentMaxWindow - 1 + startMaxWindow))
    print(arr[startMaxWindow:(currentMaxWindow + startMaxWindow)])


array = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0]
maximumSeqOneByReplaceKZero(array, 1)
