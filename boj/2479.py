import sys
N, L = map(int, input().split())

li = []

def convert(string):
    ret=0
    for i in string:
        ret*=2
        ret+=int(i)
    return ret

for i in range(N):
    li.append(convert(sys.stdin.readline().strip()))

# 1000 * 1000
# xor 연산

start, end = map(int, input().split())

graph = [[] for i in range(N+1)]

for i in range(len(li)):
    for j in range(len(li)):
        if i != j:
            if bin(li[i] ^ li[j]).count('1') == 1:
                graph[i+1].append(j+1)

#print(graph)

from collections import deque

que = deque()
que.append((start, [start]))
visit = [False for i in range(N+1)]
visit[start] = True

while que:
    point, route = que.popleft()

    if route[-1] == end:
        print(*route)
        break
    for i in graph[point]:
        if not visit[i]:
            visit[i] = True
            r = route.copy()
            r.append(i)
            que.append((i, r))
else:
    print(-1)