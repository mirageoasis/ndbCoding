from bisect import bisect_left, bisect_right
import sys
from collections import Counter

N=int(input())

chart = [[0 for j in range(N)] for i in range(4)]

first=[0 for i in range(N**2)]
second=[0 for i in range(N**2)]

for i in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    chart[0][i]=a
    chart[1][i]=b
    chart[2][i]=c
    chart[3][i]=d


for i in range(N):
    for j in range(N):
        first[i*N+j]=chart[0][i] + chart[1][j]
        second[i*N+j]=chart[2][i] + chart[3][j]

#second.sort()
c =Counter(second)
#print(first)
#print(second)

ans=0
for f in first:
    #l=bisect_left(second, -f)
    #r=bisect_right(second, -f)
    ans+= c.get(-f, 0)

print(ans)