import sys

N = int(input())

chart = []
paint = [[-1 for i in range(N)] for j in range(N)]

for i in range(N):
    chart.append(list(sys.stdin.readline()))

# 2500 * 6

def cal(N, now_row, now_col, chart, paint):
    d_r = [0, 0, 1, 1, -1, -1]
    d_c = [1, -1, 0, -1, 1, 0]
    
    paint[now_row][now_col] = 1
    color_chart = [False for i in range(4)]
    
    for i in range(6):
        new_row = now_row + d_r[i]
        new_col = now_col + d_c[i]

        if 0 <= new_row < N and 0 <= new_col < N and chart[new_row][new_col] == 'X':
            if paint[new_row][new_col] != -1:
                color_chart[paint[new_row][new_col]] = True

    now_color = 1
    
    for i in range(1, 4):
        if color_chart[i] == False:
            now_color = i
            paint[now_row][now_col] = now_color
            break

    for i in range(6):
        new_row = now_row + d_r[i]
        new_col = now_col + d_c[i]

        if 0 <= new_row < N and 0 <= new_col < N and chart[new_row][new_col] == 'X':
            if paint[new_row][new_col] == -1:
                cal(N, new_row, new_col, chart, paint)


for i in range(N):
    for j in range(N):
        if chart[i][j] == 'X' and paint[i][j] == -1:
            cal(N, i, j, chart, paint)

cnt = 0

for i in range(N):
    for j in range(N):
        if chart[i][j] == '-':
            cnt+=1

# for i in paint:
#     print(i)

if cnt == N ** 2:
    print(0)
else:
    ans = 1
    for i in range(N):
        for j in range(N):
            ans = max(ans, paint[i][j])
    print(ans)

"""
4
-XXX
X--X
X-X-
XX--
"""
