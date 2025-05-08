import sys
input=sys.stdin.readline

row_len, col_len, jump = map(int, input().split())
INF=-100 * 100 * 100 * 10000
path=[]
chart=[[INF for i in range(col_len)]for j in range(row_len)]

for i in range(row_len):
    path.append(list(map(int, input().split())))

for j in range(0, col_len):
    chart[0][j]=0

for i in range(1, row_len):
    for j in range(0, col_len):
        for row in range(i-jump, i):
            for col in range(j-jump, j+jump):
                if 0<=row<i and 0<=col<col_len:
                    if abs(row-i) + abs(col-j) <= jump:
                        if chart[i][j] < path[i][j] * path[row][col] + chart[row][col]:
                            chart[i][j] = path[i][j] * path[row][col] + chart[row][col]

# for c in chart:
#     print(c)

print(max(chart[row_len-1]))