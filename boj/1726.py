# 40

# 동1 서2 남3 북4

import sys
from collections import deque

row_len, col_len = map(int, input().split())

chart = []

for i in range(row_len):
    chart.append(list(map(int, sys.stdin.readline().split())))

src=list(map(int, input().split()))
dest=list(map(int, input().split()))

mapper={
    1: 2,
    2: 0,
    3: 1,
    4: 3
}

src[0]-=1
src[1]-=1
dest[0]-=1
dest[1]-=1


src[2]=mapper[src[2]]
dest[2]=mapper[dest[2]]
count=[[[100000 for i in range(col_len)] for j in range(row_len)] for k in range(4)]
count[src[2]][src[0]][src[1]]=0
# src랑 dest -1씩하기
# left는 +1 rigth 는 -1
# 3차원 그래프
# 0은 west 1은 south, 2는 east, 3은 north
def bfs(src, dest):
    global row_len, col_len
    que = deque()
    que.append((src[0], src[1], src[2], 0))
    dest_chart=[(0, -1), (1, 0), (0, 1), (-1, 0)]
    while que:
        #print(que)
        row, col, direct, mov = que.popleft()
        # 방향 전환
        left_idx=(direct+1) % 4
        right_idx=(direct+4-1) % 4
        if count[left_idx][row][col]>mov+1:
            count[left_idx][row][col]=mov+1
            #print(row, col, left_idx, mov+1, "a")
            que.append((row, col, left_idx, mov+1))
        if count[right_idx][row][col]>mov+1:
            count[right_idx][row][col]=mov+1
            #print(row, col, right_idx, mov+1, "b")
            que.append((row, col, right_idx, mov+1))
        
        # 거리 이동
        
        new_row_plus=dest_chart[direct][0]
        new_col_plus=dest_chart[direct][1]

        for i in range(1, 4):
            new_row = row + new_row_plus * i
            new_col = col + new_col_plus * i
            if 0<=new_row<row_len and 0<=new_col<col_len and count[direct][new_row][new_col] >= mov+1 and chart[new_row][new_col] == 0:
                count[direct][new_row][new_col]=mov+1
                que.append((new_row, new_col, direct, mov+1))
            else:
                break

bfs(src, dest)


print(count[dest[2]][dest[0]][dest[1]])