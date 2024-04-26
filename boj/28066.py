from collections import deque

N, K = map(int, input().split())

que = deque()


for i in range(1, N+1):
    que.append(i)

while len(que) >= K:
    for i in range(K):
        que.append(que.popleft())
    
    for i in range(K - 1):
        que.pop()

    #print(que)

print(que.popleft())