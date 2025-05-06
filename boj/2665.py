import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
li=[]

for i in range(n):
    li.append(list(map(int, list(input().strip()))))

chart=[[[False for k in range(n)] for j in range(n)] for i in range(101)]

que=deque()

que.append((0, 0, 0))
chart[0][0][0]=True

dr=[1, -1, 0, 0]
dc=[0, 0, -1, 1]

while que:
    row, col, time = que.popleft()
    #print(row, col, time)
    for i in range(4):
        new_row=row+dr[i]
        new_col=col+dc[i]

        if 0<=new_row<n and 0<=new_col<n:
            new_time= 0 if li[new_row][new_col] == 1 else 1
            new_time+=time
            for j in range(new_time+1):
                if chart[j][new_row][new_col]:
                    break
            else:
                chart[new_time][new_row][new_col]=True
                que.append((new_row, new_col, new_time))


for i in range(101):
    if chart[i][n-1][n-1]:
        print(i)
        break