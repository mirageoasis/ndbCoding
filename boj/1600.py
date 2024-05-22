# 2시 12분
# bfs방식을 쓰고 안에 mov를 넣어준다.

k=int(input())
col_len, row_len = map(int, input().split())

chart = []
visited = []

visited = [[[False for _ in range(col_len)] for __ in range(row_len)] for ___ in range(k+1)]

for i in range(row_len):
    chart.append(list(map(int, input().split())))

from collections import deque

def movable(new_row, new_col, left):
    if 0<=new_row<row_len and \
        0<=new_col<col_len and \
        not visited[left][new_row][new_col] \
        and chart[new_row][new_col] == 0:
        return True
    return False

def bfs():
    que = deque()
    que.append((0, 0, k, 0))
    visited[k][0][0]=True

    d_r = [-1, 1, 0, 0]
    d_c = [0, 0, -1, 1]

    # 말이 움직이는 방법
    h_r = [1, 1, -1, -1, 2, 2, -2, -2]
    h_c = [2, -2, 2, -2, 1, -1, 1, -1]
    
    while que:
        row, col, left, times = que.popleft()
        if row == row_len-1 and col==col_len-1:
            return times

        for i in range(4):
            new_row = row + d_r[i]
            new_col = col + d_c[i]
            
            if movable(new_row, new_col, left):
                visited[left][new_row][new_col]=True
                que.append((new_row, new_col, left, times+1))

        if left > 0:
            for i in range(8):
                new_row = row + h_r[i]
                new_col = col + h_c[i]
                
                if movable(new_row, new_col, left-1):
                    visited[left-1][new_row][new_col]=True
                    que.append((new_row, new_col, left-1, times+1))

    return -1

print(bfs())