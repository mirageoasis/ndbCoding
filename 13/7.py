from collections import deque
from itertools import chain

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]



N, L, R = map(int, input().split())


li = []

for i in range(N):
    li.append(list(map(int ,input().split())))


# visited 배열 모두 0
# 할 때마다 숫자 부여 1, 2....n
# 50 * 50 * 2000 * 2500

def new_check(row, col, N, visited):
    if row not in range(0, N):
        return False
    if col not in range(0, N):
        return False
    if visited[row][col]:
        return False

    return True

def bfs(li, visited, row, col, N, L, R):
    que = deque()
    # 초기 조건 설정
    total_members = []
    ret = 0
    que.append((row, col))
    visited[row][col] = True
    total_members.append((row, col))

    while que:
        row, col = que.popleft()
        
        for i in range(4):
            new_row = row + d_row[i]
            new_col = col + d_col[i]
            
            if new_check(new_row, new_col, N, visited) and abs(li[row][col] - li[new_row][new_col]) in range(L, R+1):
                visited[new_row][new_col] = True
                ret+=1
                total_members.append((new_row, new_col))
                que.append((new_row, new_col))
            #else:
            #    print((row, col), (new_row, new_col))
    
    
    mean = sum([li[row][col] for row, col in total_members]) // len(total_members)
    
    for row, col in total_members:
        li[row][col] = mean

    return ret
    
days = 0

def loop_two(N, li, visited, L, R):
    cnt=0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt+=bfs(li, visited, i, j, N, L, R)
    return cnt

days=0

while True:
    visited = [[False for i in range(N)] for i in range(N)]
    ret = loop_two(N, li, visited, L, R)
    if ret:
        days+=1
    else:
        break

print(days)