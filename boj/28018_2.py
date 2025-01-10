"""
naive하게 하자

시간 1 000 000
시간은 연속하다는 개념있죠?
"""

INF=1_000_002
import sys
n=int(input())
time_table=[0 for i in range(INF)]
for _ in range(n):
    s,e=map(int, input().split())
    time_table[s]+=1
    time_table[e+1]-=1

for i in range(1, INF):
    time_table[i]+=time_table[i-1]

m=int(input())

query=list(map(int, input().split()))

for i in query:
    print(time_table[i])