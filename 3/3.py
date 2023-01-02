'''
N K
1 될 때 까지

1. N에서 1 빼기
2. N을 K로 나눈다.
'''

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

cnt = 0

while N != 1:
    if N % K == 0:  # 0으로 떨어지지 않을 때
        N //= K
    else:
        N -= 1
    cnt+=1


print(cnt)