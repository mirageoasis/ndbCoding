from collections import deque
from copy import deepcopy
from itertools import combinations

drow = [0, 0, -1, 1]
dcol = [1, -1, 0, 0]

def cnt_0(chart):
    ans = 0
    for i in range(N):
        for j in range(M):
            if chart[i][j] == 0:
                ans += 1
    # for _ in chart:
    #     print(_)
    # print(ans)
    return ans

def bfs(c : list, virus : list, temp : list):
    
    que = deque()
    
    # 큐에 삽입
    for i in virus:
        que.append(i)
    #visited 배열
    new_chart = deepcopy(c)
    visit = deepcopy(temp)
    
    while que:
        row, col = que.popleft()

        for i in range(4):
            new_row = row + drow[i]
            new_col = col + dcol[i]
            
            if  -1 < new_row < N and -1 < new_col < M and new_chart[new_row][new_col] == 0 and visit[(new_row, new_col)] == False:
                #print(new_row, new_col, visit[(new_row, new_col)])
                new_chart[new_row][new_col] = 2
                visit[(new_row, new_col)] = True
                que.append((new_row, new_col))

    return cnt_0(new_chart)

# scan 읽어오기

chart = []
virus = []
empty = []
visited = dict()

N, M = map(int, input().split())

for _ in range(N):
    chart.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        visited[(i, j)] = False
        if chart[i][j] == 0:
            empty.append((i, j))
        elif chart[i][j] == 2:
            virus.append((i, j))
            visited[(i, j)] = True

# 벽 3개 선택
real_ans = 0

for i in combinations(empty, 3):
    a, b, c = i
    chart[a[0]][a[1]] = 1
    chart[b[0]][b[1]] = 1
    chart[c[0]][c[1]] = 1
    
    real_ans = max(bfs(chart, virus, visited), real_ans)
    
    chart[a[0]][a[1]] = 0
    chart[b[0]][b[1]] = 0
    chart[c[0]][c[1]] = 0

print(real_ans)



# bfs 수행

# 최대 찾기