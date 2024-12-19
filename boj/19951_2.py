import sys

n, m = map(int, input().split())
chart=list(map(int, input().split()))
delta=[0 for i in range(n+1)]

for i in range(m):
    start, end, d = map(int, sys.stdin.readline().split())
    start-=1
    end-=1
    
    delta[start]+=d
    delta[end+1]-=d

for i in range(1, n+1):
    delta[i]+=delta[i-1]

#print(chart)
#print(delta)

for i in range(n):
    print(chart[i]+delta[i] ,end=' ')
print()

# naive 하게 하면
# 10만 * 10만
# 하지만 부분합이다?
# 10만 쿼리도 1개의 쿼리로 가능하니까 10만만 사용하면 된다.


