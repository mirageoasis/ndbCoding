import sys
from math import gcd, lcm

R=int(input())

for i in range(R):
    M, N, x, y = map(int, sys.stdin.readline().strip().split())

    least_common_multiple = lcm(M, N)
    greast_divisor = gcd(M, N)
    cnt = 0
    while True:
        if (M * cnt + x - y) % N == 0:
            break
        if M * cnt + x > least_common_multiple:
            break
        cnt+=1
    if M * cnt + x > least_common_multiple:
        print(-1)
    else:
        print(M * cnt + x)