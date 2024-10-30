from collections import deque
import sys

chart=[]

row_len, col_len = map(int, input().split())

for i in range(row_len):
    chart.append(list(sys.stdin.readline().strip()))


