import sys
import math


ans=[0 for i in range(1001)]
s=set()
s.add((0, 1))
s.add((1, 0))
s.add((1, 1))
ans[1]=3
for i in range(2, 1001):
    adder=0
    # x
    for j in range(1, i+1):
        g=math.gcd(i, j)
        if (i//g, j//g) not in s:
            adder+=1
            s.add((i//g, j//g))
    # y
    for j in range(1, i+1):
        g=math.gcd(i, j)
        if (j//g, i//g) not in s:
            adder+=1
            s.add((j//g, i//g))
    ans[i]=ans[i-1]+adder

t=int(input())
li=[]

for i in range(t):
    a= int(sys.stdin.readline())
    print(ans[a])
