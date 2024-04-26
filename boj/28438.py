import sys
from collections import defaultdict

N, M, Q = map(int, input().split())

chart = [[0 for i in range(M)]for j in range(N)]
operation = defaultdict(int)

for _ in range(Q):
    op_type, target, num = map(int, sys.stdin.readline().split())
    operation[(op_type, target)] += num

for key, val in operation.items():
    op_type, target = key
    num = val
    target -= 1
    if op_type ==1:
        for i in range(M):
            chart[target][i] += num
    else:
        for i in range(N):
            chart[i][target] += num

for i in chart:
    print(*i)