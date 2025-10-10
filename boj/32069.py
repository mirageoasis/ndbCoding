l, n, k = map(int, input().split())
li=list(map(int, input().split()))

visit=set(li)

from collections import deque

que=deque()
ans=[]
for i in li:
    # 점과 방향
    que.append((i, 1))
    ans.append(0)
    visit.add(i)
#print(ans)

while que:
    if len(ans) >= k:
        break
    st, delta = que.popleft()

    new_pt = st + delta
    new_pt2 = st - delta
    cnt=0
    if new_pt not in visit and 0 <= new_pt < l+1:
        visit.add(new_pt)
        ans.append(delta)
        cnt+=1
    if new_pt2 not in visit and 0 <= new_pt2 < l+1:
        visit.add(new_pt2)
        ans.append(delta)
        cnt+=1
    if cnt != 0:
        que.append((st, delta+1))

for i in range(k):
    print(ans[i])