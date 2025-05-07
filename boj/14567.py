import sys
input=sys.stdin.readline

n, m = map(int, input().split())

# 자신에 의존하는 원소들 넣어주기
graph=[[] for i in range(n+1)]
ans=[0 for i in range(n+1)]

# 의존하는 개수 0개가 되면 탐색 시작
dependent=[0 for i in range(n+1)]

for _ in range(m):
    # a, b
    a, b = map(int, input().split())
    dependent[b]+=1
    
    graph[a].append(b)


from collections import deque

que=deque()

for i in range(1, n+1):
    if dependent[i] == 0:
        que.append((i, 1))
        ans[i]=1

while que:
    pt, time=que.popleft()

    for i in graph[pt]:
        dependent[i]-=1
        if dependent[i] == 0:
            que.append((i, time+1))
            ans[i]=time+1

print(*ans[1:])