import sys

M, N = map(int, input().split())

chart = []

for i in range(M):
    chart.append(list(map(int, sys.stdin.readline().split())))

# M 우주의 개수 100개
# N 행성의 개수 10000개

chart_map=[]

def binary(n_chart, target):
    start=0
    end=len(n_chart)-1
    while start<=end:
        mid=(start+end)//2
        if n_chart[mid] > target:
            end=mid-1
        elif n_chart[mid] < target:
            start=mid+1
        else:
            return mid

for c in chart:
    n_chart=list(sorted(list(set(c))))
    temp=[binary(n_chart, j) for j in c]
    chart_map.append(temp)

# for c in chart_map:
#     print(c)for c in chart_map:
#     print(c)

def is_mergable(i, j):
    one=chart_map[i]
    two=chart_map[j]

    for o, t in zip(one, two):
        if o != t:
            return False
    return True
ans=0
for i in range(M):
    # ans가 자신의 idx와 같을 때 탐색 시작
    
    for j in range(i+1, M):
        if is_mergable(i, j):
            #union(i, j)
            ans+=1

print(ans)