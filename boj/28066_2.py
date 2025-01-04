from collections import deque

n, k = map(int, input().split())

que=deque([i+1 for i in range(n)])


while True:
    if len(que) < k:
        print(que[0])
        break

    first=que[0]

    for i in range(k):
        que.popleft()
    que.append(first)
