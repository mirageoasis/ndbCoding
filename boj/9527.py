a, b = map(int, input().split(' '))

dp = [1 for i in range(100)]

for i in range(2, 100):
    dp[i] = dp[i - 1] * 2 + 2 ** (i - 2)

def digit_cal(num):
    if num == 1:
        return 1
    ret = 1
    while True:
        num //= 2
        if num < 1:
            break
        ret +=1
    
    return ret
        

def largest_2_digit(num):
    digit = digit_cal(num)
    return 2 ** (digit - 1)


def recursive_plus(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    l2d = largest_2_digit(num)
    print(num, l2d, num - l2d + 1)
    print(num - l2d + 1, recursive_plus(num - l2d))
    return (num - l2d + 1) + recursive_plus(num - l2d +1)


def cal(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    digit = digit_cal(num)
    l2d = 2 ** (digit - 1)
    lower_plus = sum([dp[i] for i in range(1, digit)])
    #print(lower_plus, num - l2d + 1, (num - l2d))
    return lower_plus + (num - l2d + 1) + cal(num - l2d)


print(cal(b) - cal(a - 1))
# print(1,cal(1))
# print(2,cal(2))
# print(3,cal(3))
# print(4,cal(4))
# print(5,cal(5))
# print(6,cal(6))
# print(7,cal(7))
# print(8,cal(8))
# print(9,cal(9))
# print(10,cal(10))
# print(11,cal(11))
# print(12,cal(12))