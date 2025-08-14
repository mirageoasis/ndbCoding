import sys
input=sys.stdin.readline

n, m = map(int, input().split())
king=input().strip()
relation=[]
claim=[]

for i in range(n):
    relation.append(input().strip().split())

for i in range(m):
    claim.append(input().strip())


# 위상정렬. 순서가 있고, 그래프가 순환하지 않음
from collections import defaultdict, deque
child_cnt=defaultdict(int)
child_set=set()
not_set=set()
child_ans=defaultdict(float)
child_set.add(king)

for c, p1, p2 in relation:
    child_set.add(c)
    not_set.add(c)
    not_set.add(p1)
    not_set.add(p2)

not_set -= child_set

for c, p1, p2 in relation:
    if p1 in child_set:
        child_cnt[c]+=1
    if p2 in child_set:
        child_cnt[c]+=1
#print(child_set, not_set)
que=deque()
que.append(king)
child_ans[king]=1
child_visit=defaultdict(bool)
child_visit[king]=True
#print(child_cnt)
while que:
    #print(que)
    cal=que.popleft()
    for c, p1, p2 in relation:
        if p1 == cal:
            child_ans[c]+=child_ans[p1]/2
            child_cnt[c]-=1
        if p2 == cal:
            child_ans[c]+=child_ans[p2]/2
            child_cnt[c]-=1
        if child_cnt[c] == 0 and not child_visit[c]:
            child_visit[c]=True
            que.append(c)
    #print(child_cnt)

ans_list=[]
for i in claim:
    ans_list.append([child_ans[i], i])

ans_list.sort(key=lambda x: -x[0])

print(ans_list[0][1])

#print(ans_list)