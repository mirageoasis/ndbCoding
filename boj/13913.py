from collections import deque

visit=[False for i in range(100001)]

n, m = map(int, input().split())
ans=""
def bfs(n, m):
    global ans
    que=deque()
    que.append((n, 0, f"{n}"))
    visit[n]=True

    while que:
        now, time, way = que.popleft()
        if now == m:
            ans=way
            return time
        
        new_one=now-1
        new_two=now+1
        new_three=now*2
        t=(new_one, new_two, new_three)

        for i in t:
            if 0<=i<=100000 and not visit[i]:
                que.append((i, time+1, way+ f" {i}"))
                visit[i]=True



print(bfs(n, m))
print(ans)