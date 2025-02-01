import sys
from collections import deque
n=int(input())

# graph 
graph=[[] for i in range(n+1)]
# 의존성 개수
dep_times=[0 for i in range(n+1)]
# 내가 걸리는 시간
my_time=[0 for i in range(n+1)]
# 앞에서 걸리는 시간 -> 동시에 해당하는 경우 max을 정해야함
primary_time=[0 for i in range(n+1)]
# 정답 시간
ans_time=[0 for i in range(n+1)]
que=deque()

for i in range(n):
    li=list(map(int, sys.stdin.readline().split()))
    
    my_time[i+1]=li[0]
    if len(li) != 2:
        li=li[1:-1]
        dep_times[i+1]=len(li)
        for j in li:
            graph[j].append(i+1)

que=deque()
# (노드, 앞에서 걸렸던 시간) 쌍으로 que에 넣어준다.
for i in range(1, len(dep_times)):
    if dep_times[i] == 0:
        que.append(i)

while que:
    node_num = que.popleft()
    # 앞의 시간
    ans_time[node_num]=primary_time[node_num]+my_time[node_num]

    for i in graph[node_num]:
        dep_times[i]-=1
        primary_time[i]=max(primary_time[i], ans_time[node_num])
        if not dep_times[i]:
            que.append(i)

for i in range(1, len(ans_time)):
    print(ans_time[i])
