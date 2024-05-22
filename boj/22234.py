import sys
from collections import deque

que = deque()

N, T, W = map(int, input().split())




# 0초 일 때 대기하는 고객
for i in range(N):
    p, t = map(int, sys.stdin.readline().split())
    que.append([p, t])

M=int(input())

arrive_dict = dict()

for j in range(M):
    p, t, c = map(int, sys.stdin.readline().split())
    arrive_dict[c-1] = [p, t]

# 대기큐 맨앞 손님

# 도착한 손님이 먼저다.
tick=0
for i in range(0, W):
    # 새로온 고객 잡기
    print(que[0][0])
    que[0][1]-=1
    if arrive_dict.get(i):
        que.append(arrive_dict[i])
    tick+=1
    if que[0][1] == 0:
        tick=0
        que.popleft()
    elif tick % T == 0:
        tick=0
        que.append(que[0])
        que.popleft()