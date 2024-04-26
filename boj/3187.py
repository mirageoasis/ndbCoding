N, M = map(int, input().split())

chart = []

for i in range(N):
    chart.append(list(input()))

visited = [[False for i in range(M)] for j in range(N)]
mass_chart = [[0 for i in range(M)] for j in range(N)]

# for c in chart:
#     print(c)

# 양 늑대

# 울타리 아니면 모두 같은 영역

'''
# 울타리
v 늑대
k 양
'''
from collections import deque

def mass(start_row, start_col, row_len, col_len, mass_cnt, visited, chart, mass_chart):
    que = deque()
    que.append((start_row, start_col))
    mass_chart[start_row][start_col] = mass_cnt
    d_r = [1, -1, 0, 0]
    d_c = [0, 0, -1, 1]

    while que:
        row, col = que.popleft()
        for i in range(4):
            new_row = row + d_r[i]
            new_col = col + d_c[i]

            if 0<=new_row<row_len and 0<=new_col<col_len and not visited[new_row][new_col] and chart[new_row][new_col] != '#':
                visited[new_row][new_col] = True
                mass_chart[new_row][new_col] = mass_cnt
                que.append((new_row, new_col))


mass_cnt=1
for i in range(N):
    for j in range(M):
        if not visited[i][j] and chart[i][j] != '#':
            visited[i][j] = True
            mass(i, j, N, M, mass_cnt, visited, chart, mass_chart)
            mass_cnt+=1

wolf_cnt = 0
sheep_cnt=0

# 이제 영역에서 각각 늑대 양을 센다

for now_mass in range(mass_cnt):
    temp_wolf_cnt=0
    temp_sheep_cnt=0

    for i in range(N):
        for j in range(M):
            if mass_chart[i][j] == now_mass:
                if chart[i][j] == 'v':
                    temp_wolf_cnt+=1
                elif chart[i][j] == 'k':
                    temp_sheep_cnt+=1
    if temp_wolf_cnt >= temp_sheep_cnt:
        wolf_cnt+=temp_wolf_cnt
    else:
        sheep_cnt+=temp_sheep_cnt

print(sheep_cnt, wolf_cnt)