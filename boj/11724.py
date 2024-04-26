from collections import deque

# Vertex, 

N, M = map(int, input().split(' '))

visit = [0 for i in range(N + 1)]

chart = [[] for j in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split(' '))

    chart[a].append(b)
    chart[b].append(a)


ans=0

for i in range(1, N+1):
    if visit[i] != 0:
        continue
    
    q = deque()

    q.append(i)

    while q:
        k = q.pop()
        for j in chart[k]:
            if not visit[j]:
                visit[j] = 1
                q.append(j)

    ans+=1

print(ans)