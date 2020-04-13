# Problem https://leetcode.com/problems/palindrome-number/

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x < 10:
        return True
    elif 10 <= x <= 99:
        if x % 11 == 0:
            return True
        return False

    res = [int(i) for i in str(x)]
    l = len(str(x))
    mid = 0
    if len(str(x)) % 2 == 0:
        mid = int(l / 2)
    else:
        mid = int(l / 2) + 1

    i = 0
    while i < mid:
        if res[i] != res[l - 1 - i]:
            return False
        i += 1

    return True

#Second Solution
def isPalindrome1(self, x):
    if x < 0 or (x > 0 and x % 10 == 0):
        return False

    return x == self.reverseUtil(x)

def reverseUtil(self, x):
    result = 0

    while x != 0:
        digit = x % 10
        result = result * 10 + digit
        x = int(x / 10)

    return result


#Third Solution
def isPalindrome(self, x):
    if x < 0:
        return False
    else:
        x_str = str(x)
        i = 0
        j = len(x_str) - 1

        if j == 0:
            return True

        while (x_str[i] == x_str[j]) and (i <= j):
            i = i + 1
            j = j - 1

        if i < j:
            return False
        else:
            return True


num1 = 121
num2 = -121
num3 = 10
num4 = 1
num5 = 23
num6 = 55
num7 = 1001
num8 = 1000030001

print(isPalindrome(num1))
