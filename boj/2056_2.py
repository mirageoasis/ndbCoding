from collections import deque
n=int(input())

graph=[[] for i in range(n+1)]
dep=[0 for i in range(n+1)]
times=[0 for i in range(n+1)]
final=[0 for i in range(n+1)]

for i in range(n):
    li = list(map(int, input().split()))

    times[i+1]=li[0]
    final[i+1]=li[0]
    dep[i+1]=li[1]
    for j in range(li[1]):
        graph[li[2+j]].append(i+1)

#print(dep)
#print(graph)

que = deque()

for i in range(1, n+1):
    if not dep[i]:
        que.append(i)

while que:
    pt=que.popleft()

    for i in graph[pt]:
        dep[i]-=1
        final[i]=max(final[i], times[i]+final[pt])

        if dep[i] == 0:
            que.append(i)

#print(final)
print(max(final))