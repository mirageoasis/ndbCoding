# 일단 dp, 그리디, 이분탐색

# 근데 이분탐색은 아닌거 같고

# 아니면 숫자가 순서대로 있다는 것이 힌트인거 같기도 한데

# bfs인거 같은데? ㄷㄷ
# 일단 같은 index는 잡는다.
import sys
input=sys.stdin.readline
n=int(input())

li=[]
li.append(-1)
for i in range(n):
    li.append(int(input()))

pick=set()
for i in range(1, n+1):
    if li[i] == i:
        pick.add(i)

# pick에 있으면 해당 bfs는 무효
from collections import deque
for i in range(1, n+1):
    que=deque()
    if i in pick:
        continue
    que.append(i)
    flag=False
    visit=[False for i in range(n+1)]
    origin=i
    visit[i]=True
    while que:
        pt = que.popleft()
        new_pt = li[pt]
        if new_pt in pick:
            break
        if new_pt == origin:
            flag=True
            break
        if visit[new_pt]:
            break
        visit[new_pt]=True
        que.append(new_pt)
    #print(pick, flag)
    if flag:
        # visit 찾아서 추가
        for i in range(1, n+1):
            if visit[i]:
                pick.add(i)


print(len(pick))

for i in list(sorted(list(pick))):
    print(i)
