import sys
input=sys.stdin.readline
n=int(input())
chart=[]
INF=9999999999999999
dp=[[INF for i in range(3)] for j in range(n)]
for i in range(n):
    chart.append(list(map(int, input().split())))
# x번 index이고 now_color색일 때 가지는 최소값
def cal(index, now_color, origin_color):
    global INF
    if index == 0:
        return chart[0][now_color]
    if dp[index][now_color] != INF:
        return dp[index][now_color]

    mini=INF
    for i in range(3):
        if i == now_color:
            continue
        if index == 1 and i == origin_color:
            continue
        mini=min(mini, cal(index-1, i, origin_color))
    dp[index][now_color]=mini + chart[index][now_color]
    return dp[index][now_color]

ans=cal(len(chart) - 1, 0, 0)
dp=[[INF for i in range(3)] for j in range(n)]
ans=min(ans, cal(len(chart) - 1, 1, 1))
dp=[[INF for i in range(3)] for j in range(n)]
ans=min(ans, cal(len(chart) - 1, 2, 2))

print(ans)