n=int(input())

first=[]
second=[]
third=[]
fourth=[]
import sys
for i in range(n):
    a,b,c,d=map(int, sys.stdin.readline().split())
    first.append(a)
    second.append(b)
    third.append(c)
    fourth.append(d)
all_first=[0] * (n**2)
all_second=[0] * (n**2)
for i in range(n):
    for j in range(n):
        all_first[i*n+j] = first[i] + second[j]
        all_second[i*n+j] = third[i] + fourth[j]

all_second.sort()

from bisect import bisect_left, bisect_right
ans=0
for i in all_first:
    a=bisect_left(all_second, -i)
    b=bisect_right(all_second, -i)
    #print(i, b-a)
    ans+=(b-a)

print(ans)