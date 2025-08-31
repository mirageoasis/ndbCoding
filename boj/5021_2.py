from collections import defaultdict, deque
n, m = map(int, input().split())

king=input()
li=[]
for i in range(n):
    li.append(input().split())

parent=set()
dep_graph=defaultdict(int)
score=dict()

parent.add(king)
for a, b, c in li:
    parent.add(a)

for a, b, c in li:
    if b in parent:
        dep_graph[a]+=1
    if c in parent:
        dep_graph[a]+=1

que=deque()
que.append(king)
score[king]=1

for a, b, c in li:
    if b not in parent:
        score[b]=0
    if c not in parent:
        score[c]=0

while que:
    now = que.popleft()
    for a, b, c in li:
        if b == now:
            dep_graph[a]-=1
        if c == now:
            dep_graph[a]-=1
        
        if dep_graph[a] == 0 and a not in score.keys():
            score[a] = (score[b] + score[c]) / 2
            que.append(a)

candi=[]
for i in range(m):
    c=input()
    if c in score.keys():
        candi.append((score[c], c))
    else:
        candi.append((0, c))

candi.sort(reverse=True)
print(candi[0][1])