# 3시 06분 시작

import sys
from collections import defaultdict, deque

chart_len, case_len=map(int, input().split())

chart=[[False for i in range(chart_len)] for j in range(chart_len)]
visit=[[False for i in range(chart_len)] for j in range(chart_len)]
light_list=defaultdict(list)

for i in range(case_len):
    a, b, c, d = map(int, sys.stdin.readline().split())
    
    light_list[(a-1, b-1)].append((c-1, d-1))

#print(light_list)

def bfs():
    global chart_len
    candidate=set()
    que=deque()
    chart[0][0]=True
    visit[0][0]=True
    que.append((0, 0))

    d_r=[0, 0, -1, 1]
    d_c=[1, -1, 0, 0]

    while que:
        now_row, now_col = que.popleft()

        if (now_row, now_col) in light_list:
            for a,b in light_list[(now_row, now_col)]:
                chart[a][b]=True
                if (a,b) in candidate:
                    que.append((a, b))
                    candidate.remove((a,b))
                    visit[a][b]=True
        
        for i in range(4):
            new_row=now_row+d_r[i]
            new_col=now_col+d_c[i]

            if 0<=new_row<chart_len and 0<=new_col<chart_len and not visit[new_row][new_col]:
                if chart[new_row][new_col]:
                    visit[new_row][new_col]=True
                    que.append((new_row, new_col))
                else:
                    candidate.add((new_row, new_col))

bfs()

ans=0
for i in range(chart_len):
    for j in range(chart_len):
        if chart[i][j]:
            ans+=1

print(ans)