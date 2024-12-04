import sys

n, m = map(int, input().split())

# 점 1000개 아님?
# 이거 그냥 플로이드 와샬인데
# 특히, 추후에 여러개 케이스를 준다는거 보면 모든 결과를 구해야함
INF=999999
chart=[[INF for i in range(n+1)] for j in range(n+1)]
cord=dict()
teleport=set()

for i in range(1, n+1):
    li=list(map(int, sys.stdin.readline().split()))

    if li[0] == 1:
        teleport.add(i)
    cord[i]=(li[1], li[2])

#print(cord)
#print(teleport)

for i in range(1, n+1):
    chart[i][i]=0

# 직통 거리 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        i_cord=cord[i]
        j_cord=cord[j]
        comp=abs(i_cord[0] - j_cord[0]) + abs(i_cord[1] - j_cord[1])
        
        if i in teleport and j in teleport:
            if m < comp:
                comp=m
        
        if chart[i][j] > comp:
            chart[i][j]=comp


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if chart[i][j] > chart[i][k] + chart[k][j]:
                chart[i][j] = chart[i][k] + chart[k][j]


t = int(input())

for i in range(t):
    first, second = map(int, sys.stdin.readline().split())

    print(chart[first][second])

