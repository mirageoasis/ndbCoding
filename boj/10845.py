# 3시 48분
from collections import deque
from sys import stdin

N=int(input())
que=deque()

for i in range(N):
    cmd=stdin.readline().strip()
    li=cmd.split(" ")

    if li[0] == "push":
        que.append(int(li[1]))
    elif cmd == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        print(1 if not que else 0)
    elif cmd == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif cmd == "back":
        if que:
            print(que[-1])
        else:
            print(-1)
