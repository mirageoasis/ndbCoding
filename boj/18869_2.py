"""
naive 하게 해보자

m = 100
n = 10000

naive하게하면 
10000 * 10000 비교를 한다. 어떻게 100 * 100 / 2개가
1억 * 5만

1억개를 고쳐야한다.

만약에 n번째 큰 수라고 정할 수 있다면?
하나당

nlogn =>
nlogn으로 위치 찾기
10000 * 5 * 100 => 5백만

5000천개를 비교한다면 비교 1개당

1만 
대략 0.5초
"""
import sys
from bisect import bisect_left
n, m = map(int, input().split())

old_graph=[]
# 순서를 나열한 집합이 있는 곳
new_graph=[]

for i in range(n):
    li=list(map(int, sys.stdin.readline().split()))

    old_graph.append(li)

for idx, val in enumerate(old_graph):
    #print(val)
    num_set=list(sorted(set(val)))
    temp_list=[]
    for i in val:
        temp_list.append(bisect_left(num_set, i))
    new_graph.append(temp_list)

def cmp(first, second):
    for a, b in zip(first, second):
        if a!= b:
            return False
    return True

ans=0
for i in range(n):
    for j in range(i+1, n):
        if cmp(new_graph[i], new_graph[j]):
            ans+=1

print(ans)