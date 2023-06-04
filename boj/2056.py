from collections import deque
N=int(input())
chart = [[] for _ in range(N+1)]
working_time = [0]
ans = [0]
topo_count=[0 for _ in range(N+1)]
topo_sort=[]
que = deque()

for i in range(1,N+1):
    temp=list(map(int, input().split()))
    working_time.append(temp[0])
    ans.append(temp[0])
    topo_count[i] = len(temp[2:])
    for j in temp[2:]:
        chart[j].append(i)

#print(chart)

for i in range(1,N+1):
    if topo_count[i] == 0:
        que.append(i)
#print(topo_count)
#print(que)

while que:
    t = que.popleft()
    topo_sort.append(t)
    for i in chart[t]:
        topo_count[i]-=1
        ans[i] = max(working_time[i]+ans[t], ans[i])
        if topo_count[i] == 0:
            que.append(i)
    
    #print(topo_count)    

#print(topo_sort)
print(max(ans))