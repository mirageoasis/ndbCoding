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