# Print all subarrays with 0 sum
# Given an array of integers, print all sub-arrays with 0 sum.
# Input:  arr = [6, 3, -1, -3, 4, -2, 2,4, 6, -12, -7]
# Subarray found from Index 2 to 4
# Subarray found from Index 2 to 6
# Subarray found from Index 5 to 6
# Subarray found from Index 6 to 9
# Subarray found from Index 0 to 10

def findSubArrays(arr):
    hashmap = {}
    out = []
    sum = 0

    for i in range(0, len(arr)):
        sum += arr[i]
        newArr = []

        if sum == 0:
            out.append((0, i))

        if sum in hashmap:
            newArr = hashmap.get(sum)
            for j in range(len(newArr)):
                out.append([newArr[j] + 1, i])

        newArr.append(i)
        hashmap[sum] = newArr

    return out


arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
print(findSubArrays(arr))