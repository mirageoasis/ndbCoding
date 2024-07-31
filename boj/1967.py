#  55분
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
# bottom to top 으로 가면서 더해서 거리를 구하고 -> 여러개중 2개를 합쳐서 거리를 찾아보고
#  노드의 값은 여러개중 최대값으로 하는 것으로

chart=defaultdict(list)

N=int(input())
ans=0
# 부모 작은 순서대로

for i in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    chart[a].append([b, c])

def dfs(now):
    global ans
    #print(now)
    if len(chart[now]) == 0:
        return 0
    if len(chart[now]) == 1:
        ret = dfs(chart[now][0][0]) + chart[now][0][1]
        ans=max(ans, ret)
        return ret
    
    # 노드 최대 값 + 자신과의 거리
    li = []
    for node, value in chart[now]:
        li.append(dfs(node) + value)
    
    li.sort(reverse=True)
    ans=max(ans, li[0]+li[1])

    return li[0]

dfs(1)

print(ans)