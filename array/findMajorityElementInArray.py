# Find majority element in an array (Boyer–Moore majority vote algorithm)
# Given an array of integers containing duplicates, return the majority element
# in an array if present. A majority element appears more than n/2 times where n is the size of the array.
# The majority element is 2 in the array {2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2}

from typing import List


def findMajorityInArray(arr: List[int]):
    hashtable = {}

    for i in range(len(arr)):
        if arr[i] in hashtable:
            hashtable[arr[i]] += 1
            if hashtable[arr[i]] >= len(arr) / 2:
                print("Majority element: ", arr[i])
        else:
            hashtable[arr[i]] = 1


def boyermooreMajorityVote(arr: List[int]):
    candidate = 0
    counter = 0
    for i in range(len(arr)):
        if counter == 0:
            candidate = arr[i]
            counter = 1
        else:
            if arr[i] == candidate:
                counter += 1
            else:
                counter -= 1

    print("Majority element: ", candidate)


array = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
findMajorityInArray(array)
boyermooreMajorityVote(array)