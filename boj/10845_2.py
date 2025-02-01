from collections import deque
n=int(input())
que=deque()
import sys
for i in range(n):
    t=sys.stdin.readline().strip()

    if t.startswith("push"):
        que.append(int(t.split()[-1]))
    elif t == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif t == "back":
        if que:
            print(que[-1])
        else:
            print(-1)
    elif t == "size":
        print(len(que))
    elif t == "empty":
        print(0 if len(que) else 1)
    elif t == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)
