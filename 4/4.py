'''
starting position

0북 1 동 2 남 3서

4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
1 은 바다 0 은 육지
'''
import sys
import time

N, M = map(int, sys.stdin.readline().rstrip().split())
r, c, direction = map(int, sys.stdin.readline().rstrip().split())

# 더할 때 +3 해주면 된다.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

chart  = []

for i in range(N):
    chart.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 만약 도착하면 2로 바꿔준다.
while True:
    # 1 그냥 수 있다.
    # 2 회전해서 간다
    # 뒤로 빠꾸
        # 막장
    nr = r + dr[direction]
    nc = c + dc[direction]
    #print(nr, nc)
    # 바운더리 check 는 필요 없다. 테두리는 죄다 바다임
    chart[r][c] = 2
    if chart[nr][nc] == 0:
        # 바로 이동
        r, c = nr, nc
    else:
        # 기다렸다가 이동
        for i in range(3):
            direction +=3
            direction %=4
            nr = r + dr[direction]
            nc = c + dc[direction]
            if chart[nr][nc] == 0:
                r, c = nr, nc
                break
        else:
            # 회전해도 못 찾음
            direction +=3
            direction %=4
            nr = r - dr[direction]
            nc = c - dc[direction]
            if chart[nr][nc] == 1:
                break
            elif chart[nr][nc] == 2:
                r, c = nr, nc
            else:
                print("에러 났음")
    # 2의 개수를 센다.

cnt = 0
for i in range(N):
    for j in range(N):
        if chart[i][j] == 2:
            cnt+=1
print(cnt)