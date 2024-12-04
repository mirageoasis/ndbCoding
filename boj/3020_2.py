from bisect import bisect_left
import sys

n, m = map(int, input().split())

# 논리의 회로를 보자

# 
li=[]
for i in range(n):
    li.append(int(sys.stdin.readline()))

lower=[val for idx, val in enumerate(li) if not idx % 2]
upper=[val for idx, val in enumerate(li) if idx % 2]

lower.sort()
upper.sort()

ans=[]
for i in range(1, m+1):
    lower_cnt=len(lower)-bisect_left(lower, i)
    upper_cnt=len(upper)-bisect_left(upper, m-i+1)
    #print(i, lower_cnt, upper_cnt)
    ans.append(lower_cnt+upper_cnt)


print(min(ans), ans.count(min(ans)))