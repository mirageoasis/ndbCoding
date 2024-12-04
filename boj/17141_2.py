from collections import deque
from itertools import combinations

n, m = map(int, input().split())

chart=[]

def debug(target_chart):
    for c in target_chart:
        print(c)

for i in range(n):
    chart.append(list(map(int, input().split())))

two_list=[]

for i in range(n):
    for j in range(n):
        if chart[i][j] == 2:
            two_list.append((i, j))


def bfs(new_chart, n, que):
    
    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]

    while que:
        now_row, now_col, now_time = que.popleft()
        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]

            if 0<=new_row<n and 0<=new_col<n and new_chart[new_row][new_col] == -1:
                new_chart[new_row][new_col]=now_time+1
                que.append((new_row, new_col, now_time+1))



ans=999999
for start in combinations(two_list, r=m):
    que=deque()
    new_chart=[[-1 for i in range(n)] for j in range(n)]

    # 막힌 곳은 -2 처리
    # 뚫린 곳은 -1 처리
    for i in range(n):
        for j in range(n):
            if chart[i][j] == 1:
                new_chart[i][j]=-2

    # 0을 넣어준다.
    for s in start:
        new_chart[s[0]][s[1]]=0
        que.append((s[0], s[1], 0))
    
    bfs(new_chart, n, que)

    maxi=-1
    # new_chart가 -1인 곳이 존재하면 out!
    flag=False
    for i in range(n):
        for j in range(n):
            if new_chart[i][j] == -1:
                flag=True
                break
    
    if flag:
        continue
    
    # 최대 시간 구하기
    for i in range(n):
        for j in range(n):
            maxi=max(maxi, new_chart[i][j])

    ans=min(ans, maxi)

    #print(que)

print(ans if ans != 999999 else -1)