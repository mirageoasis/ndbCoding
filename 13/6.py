from copy import deepcopy
from collections import deque
from itertools import combinations

def rng(row, col, N):
    if row not in range(0, N):
        return False
    if col not in range(0, N):
        return False
    return True
    
d_row = [0, 0, -1, 1]
d_col = [1, -1, 0, 0]

def find_yes(chart, t_q: deque, N):
    while t_q:
        row, col, dir = t_q.popleft()

        new_row = row + d_row[dir]
        new_col = col + d_col[dir]
        if rng(new_row, new_col, N):
            if chart[new_row][new_col] == "X" or chart[new_row][new_col] == "T":
                t_q.append((new_row, new_col, dir))
                chart[new_row][new_col] = "T"
            elif chart[new_row][new_col] == "S":
                # for i in chart:
                #     print(i)
                # print()
                return False
    return True

N = int(input())
chart = []
t_q = deque()
room = []

for i in range(N):
    chart.append(input().split())

# 초기 설정
for i in range(N):
    for j in range(N):
        if chart[i][j] == "T":
            t_q.append((i, j, 0))
            t_q.append((i, j, 1))
            t_q.append((i, j, 2))
            t_q.append((i, j, 3))
        elif chart[i][j] == "X":
            room.append((i, j))

for i in combinations(room ,3):
    a, b, c = i
    new_chart = deepcopy(chart)
    new_t_q = deepcopy(t_q)
    new_chart[a[0]][a[1]] = "O"
    new_chart[b[0]][b[1]] = "O"
    new_chart[c[0]][c[1]] = "O"
    if(find_yes(new_chart, new_t_q, N)):
        print("YES")
        break
else:
    print("NO")