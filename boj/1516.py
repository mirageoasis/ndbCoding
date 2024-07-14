import sys
from collections import defaultdict
# 11시 46분 시작
N=int(input())

data = defaultdict(list)
cnt = defaultdict(int)
time_dict = defaultdict(int)
# topology sort
for i in range(N):
    t = list(map(int, sys.stdin.readline().split()))[:-1]
    time=t[0]
    e= [] if len(t) == 1 else t[1:]
    
    time_dict[i+1]=time
    cnt[i+1]=len(e)
    for j in e:
        data[j].append(i+1)

#data = [[k,v] for k, v in data.items()]

from collections import deque
next=deque()
ans={k:v for k, v in time_dict.items()}

for k, v in cnt.items():
    if v==0:
        next.append([k, v])

# print(data)
# print(cnt)
# print(time_dict)
# print()

while next:
    k, _ = next.popleft()
    for i in data[k]:
        ans[i]=max(time_dict[i]+ans[k], ans[i])
        cnt[i]-=1
        if cnt[i] == 0:
            next.append([i, data[i]])
    #print(cnt)
    #print(ans)

for k, v in ans.items():
    print(v)

"""
위상 정렬에서 list를 쓰는 것도 가능은하나...
queue라는 더 좋은 자료형이 있으므로... 궅이 쓰지말자!

위상 정렬에는 2가지 자료형이 필요
1. 의존하는 노드 개수를 세는 배열
2. 자신에게 의존하는 노드의 정보를 담은 배열

1번 배열에서 개수가 0개인 노드를 찾아서 큐에 넣는다.
1번 배열을 queue에서 pop하면서 2번 배열 정보를 통해 1번 배열에서 의존 개수를 -1해준다. 이 때, 의존 개수가 0이되면 queue에 넣어준다.


이 문제를 단순 위상정렬이라고 생각해서 문제였음
1 2 3 건물이 있을 때 

3번 건물이 1 2 에 의존하고
1 2 는 아무 건물에도 의존하지 않을 때 단순히
1 2의 노드를 탐색하는 과정에서 3번 비용에 1과 2의 시간을 더해준다면 
1과 2는 병렬적으로 실행될 수 있지만 직렬로 되는 효과가 발생.
그러므로 1과 2의 노드를 탐색할 때, 3의 노드에는 max 를 적용
시간이 더 걸리는 쪽을 선택한다.
"""
