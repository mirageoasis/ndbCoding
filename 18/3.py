# 집, 도로의 수 
N, M = map(int, input().split())

chart = []

def union(parent, a, b):
    a_p = parent[a]
    b_p = parent[b]
    if a_p >= b_p:
        parent[a_p] = b_p
    else:
        parent[b_p] = a_p

def parent_find(parent, a):
    if parent[a] != a:
        parent[a] = parent_find(parent, parent[a])
    return parent[a]

for _ in range(M):
    chart.append(list(map(int, input().split())))


'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''

chart.sort(key=lambda x : x[2])

ans=0
parent = [i for i in range(N+1)]
cnt=0
for i in chart:
    if cnt == N:
        break
    start, end, distance = i

    if parent_find(parent, start) != parent_find(parent, end):
        
        union(parent, start, end)
        #print(i)
        ans+=distance
        cnt+=1
    else:
        continue
#print(ans)
t = 0
for i in chart:
    a,b, c = i
    t+=c

print(t-ans)