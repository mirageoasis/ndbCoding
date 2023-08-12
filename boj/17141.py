import sys
from copy import deepcopy
from collections import deque
from itertools import combinations, permutations

INF = 9999999999

N, M = map(int, input().split())

chart = []
target_list = []
wall_list = []

for i in range(N):
    chart.append(list(map(int, sys.stdin.readline().strip().split())))

# for i in chart:
#     print(i)

def check_total(chart, N):
    for i in range(N):
        for j in range(N):
            if chart[i][j] == 0:
                return False
    return True

def bound_check(new_row, new_col, N):
    if new_row < 0:
        return False
    if new_col < 0:
        return False
    if new_row > N - 1:
        return False
    if new_col > N - 1:
        return False
    return True

def cal(points, c, wall_list, N):
    chart = deepcopy(c)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 바이러스 가능하나 없는 공간은 0으로 처리

    for i in range(N):
        for j in range(N):
            if chart[i][j] == 2 and not ((i, j) in points or (j, i) in points):
                chart[i][j] = 0

    que = deque()
    # point 넣어준다.
    for i in points:
        r, c = i
        que.append((r, c, 0))

    while que:
        row, col, time = que.popleft()
        #print(row, col, time)
        for i in range(4):
            new_row = row + dx[i]
            new_col = col + dy[i]
            #print(new_row, new_col)
            if bound_check(new_row, new_col, N) and chart[new_row][new_col] == 0:
                que.append((new_row, new_col, time+1))
                chart[new_row][new_col] = time+1
    
    if not check_total(chart, N):
        return INF

    for i in points:
        r, c = i
        chart[r][c] = 0
    # 벽도 걸러야

    for i in wall_list:
        r, c = i
        chart[r][c] = 0

    #for i in chart:
    #    print(i)
    #print()
    return max(list(map(max, chart)))

for i in range(N):
    for j in range(N):
        if chart[i][j] == 2:
            target_list.append((i, j))
        elif chart[i][j] == 1:
            wall_list.append((i, j))

ans = INF

for i in combinations(target_list, M):
    ans = min(ans, cal(i, chart, wall_list, N))

if ans == INF:
    print(-1)
else:
    print(ans)


