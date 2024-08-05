#51분 시작
from collections import deque

f, s, g, u, d = map(int, input().split())

visit=[False for i in range(f+1)]

ans=9999999999
que=deque()

que.append((s, 0))
visit[s]=True

while que:
    now,m=que.popleft()
    #print(now, m)
    if now == g:
        ans=m
        break

    mov=[u, -d]

    for i in range(2):
        new_loc=now+mov[i]
        if 1<=new_loc<=f and not visit[new_loc]:
            visit[new_loc]=True
            que.append((new_loc,m+1))

if ans == 9999999999:
    print("use the stairs")
else:
    print(ans)