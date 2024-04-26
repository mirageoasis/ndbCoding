import sys
import copy
from collections import deque

N, Q = map(int, input().split())

chart = []

for i in range(2 ** N):
    chart.append(list(map(int, sys.stdin.readline().split())))

command = list(map(int, sys.stdin.readline().split()))

real_size = 2 ** N

for c in command:
    one_line = 2 ** c

    time = 0
    
    saved_chart = copy.deepcopy(chart)
    for s_row in range(0, real_size, one_line):
        for s_col in range(0, real_size, one_line):
            for row in range(0, one_line):
                for col in range(0, one_line):
                    chart[s_row + (col)][s_col + (one_line - row - 1)] = saved_chart[s_row + row][s_col + col]
    
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    saved_chart = copy.deepcopy(chart)
    for row in range(real_size):
        for col in range(real_size):
            cnt = 0
            for i in range(4):
                new_row = row + dr[i]
                new_col = col + dc[i]
                if 0 <= new_row < real_size and 0 <= new_col < real_size:
                    if saved_chart[new_row][new_col] > 0:
                        cnt+=1
            if cnt < 3:
                chart[row][col] -= 1

ans=0
for i in range(real_size):
    for j in range(real_size):
        if chart[i][j] > 0:
            ans+=chart[i][j]

print(ans)

def bfs(real_size, row, col, mark, chart, visited):
    que = deque()
    que.append((row, col))
    chart[row][col] = mark

    while que:
        r, c = que.popleft()
        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]
        
        for i in range(4):
            new_row = r + dr[i]
            new_col = c + dc[i]
            if 0 <= new_row < real_size and 0 <= new_col < real_size:
                if not visited[new_row][new_col] and chart[new_row][new_col] > 0:
                    visited[new_row][new_col] = True
                    chart[new_row][new_col] = mark
                    que.append((new_row, new_col))

visited = [[False for i in range(real_size)] for j in range(real_size)]
mark = 1

for i in range(real_size):
    for j in range(real_size):
        if chart[i][j] > 0 and not visited[i][j]:
            bfs(real_size, i, j, mark, chart, visited)
            mark +=1

ans=0
for i in range(1, mark):
    tmp = 0
    for row in range(real_size):
        for col in range(real_size):
            if chart[row][col] == i:
                tmp+=1
    ans = max(ans, tmp)

print(ans)
"""
2 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
1 2
"""
