# Problem : https://leetcode.com/problems/reverse-integer/
# Given a 32-bit signed integer, reverse digits of an integer.

num1 = 123
num2 = -123
num3 = 120
num4 = -120
num5 = -120000
num6 = 1534236469


# print(str(num1)[3:None:-1])
# print(str(num2)[3:0:-1])
# print(str(num3)[1:None:-1])
# print(str(num4)[2:0:-1])
# print(str(num5)[2:0:-1])

def reverse1(x):
    result = 0
    if x < 0:
        symbol = -1
        x = -x
    else:
        symbol = 1
    while x:
        result = (result * 10) + (x % 10)
        x = int(x/10)
    return 0 if int(result) > pow(2, 31) - 1 or int(result) < -pow(2, 31) else int(result)*symbol


def reverse(x: int) -> int:
    s = str(x)
    index = len(s) - 1
    result = ''
    while int(s[index]) == 0:
        if index > 0:
            index -= 1
        elif index == 0:
            break
        if int(s[index]) != 0:
            break
    for i in range(index, -1, -1):
        result += s[i]
    if x < 0:
        result = result[:-1]
        result = '-' + result
    return 0 if int(result) > pow(2, 31) - 1 or int(result) < -pow(2, 31) else int(result)


print(reverse1(num1))
