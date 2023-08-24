import sys
from collections import defaultdict
from collections import deque

N=int(input())
M=int(input())

dic = defaultdict(list)
conn = defaultdict(set)

def cal(start):
    que= deque()
    
    que.append(start)

    visit = [False for i in range(N+1)]

    while que:
        a = que.popleft()
        conn[a].add(start)
        conn[start].add(a)
        for i in dic[a]:
            if not visit[i]:
                que.append(i)
                visit[i] = True

for i in range(1, N+1):
    dic[i] = []
    conn[i] = set()

for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    dic[b].append(a)

for start in range(1, N+1):
    cal(start)

for key, value in conn.items():
    print(N - len(value))
