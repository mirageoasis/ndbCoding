# 10 ** 11
A, B, C = map(int, input().split())



def cal(a, b, c):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return cal(a, b // 2, c) ** 2 % c
    
    return (cal(a, b // 2, c) * cal(a, b // 2 + 1, c)) % c




print(cal(A, B, C))