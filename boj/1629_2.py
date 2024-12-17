a, b, c = map(int, input().split())

def cal(a, b, c):

    if b == 1:
        return a % c

    if not b % 2:
        return cal(a, b//2, c) ** 2 % c

    return (cal(a, b//2, c) * cal(a, b - b//2, c)) % c

print(cal(a, b, c))