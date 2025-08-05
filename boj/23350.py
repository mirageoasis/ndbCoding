# 우선 순위가 낮은 경우를 먼저 적제한다.
# 우선 순위가 같다면 스택에서 꺼내고 다시 적재 ㄱ
# 완전탐색으로 해도 문제 없으나 그래도 stack으로...


# 일단 무게 별로 count
# 그리고 무거운 컨테이너 꺼낼 때 stack으로

from collections import deque
import sys

input = sys.stdin.readline
num, kind = map(int, input().split())
que = deque()
pri_count=[0 for i in range(kind+1)]

for i in range(num):
    pri, weight = map(int, input().split())
    que.append([pri, weight])
    pri_count[pri]+=1


ans=0
now_lvl = kind

stack=[]
while que:
    #print(stack)
    pri, weight = que.popleft()

    if now_lvl != pri:
        que.append([pri, weight])
        ans+=weight
        continue
    
    # 같다면
    temp_stack=[]
    #print(37)
    while stack:
        new_pri, new_weight = stack[-1]
        if new_weight < weight and pri == new_pri:
            ans+=new_weight
            temp_stack.append(stack.pop())
        else:
            break
    stack.append([pri, weight])
    while temp_stack:
        new_pri, new_weight = temp_stack.pop()
        ans+=new_weight
        stack.append([new_pri, new_weight])
    ans+=weight
    pri_count[pri]-=1
    if pri_count[pri] == 0:
        now_lvl-=1
#print(que)
#print(stack)
print(ans)