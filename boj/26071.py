import sys

N=int(input())

chart = []

for i in range(N):
    chart.append(sys.stdin.readline().strip().strip())

# for i in chart:
#     print(i)

max_row = -1
min_row = 1501
max_col = -1
min_col = 1501
cnt=0

for i in range(N):
    for j in range(N):
        if chart[i][j] == 'G':
            cnt+=1
            max_row = max(i, max_row)
            max_col = max(j, max_col)
            min_row = min(i, min_row)
            min_col = min(j, min_col)

ans = 0

if max_row !=  min_row:
    ans += min(max_row, N - 1 - min_row)
if max_col != min_col:
    ans += min(max_col, N - 1 - min_col)

if cnt == 1:
    print(0)
else:
    print(ans)