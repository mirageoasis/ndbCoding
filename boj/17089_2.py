"""
3명을 고르는게 이슈

dp bfs greedy 
3사람 모두 친구
"""
import sys
n, m = map(int, input().split())
root=[[] for i in range(n+1)] # 자신보다 큰 숫자만 넣어준다.
temp_graph=[[] for i in range(n+1)] # 자신보다 큰 숫자만 넣어준다.
f=[]
# 그냥 친구들 추가해서 줄여주기?
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    f.append((min(a, b), max(a, b)))

f.sort(key=lambda x: (x[0], x[1]))

for a, b in f:
    temp_graph[a].append(b)
    root[a].append(b)
    root[b].append(a)

#print(temp_graph)

mini=999999999
for i in range(1, n+1):
    now_graph=temp_graph[i]

    if len(now_graph) < 2:
        continue
    # 작은게 i
    for first in range(len(now_graph)):
        for second in range(first+1,len(now_graph)):
            if now_graph[second] in temp_graph[now_graph[first]]:
                #print(i, now_graph[first], now_graph[second])
                mini=min(mini, len(root[now_graph[first]]) + len(root[now_graph[second]]) + len(root[i]) - 6)

if mini == 999999999:
    print(-1)
else:
    print(mini)