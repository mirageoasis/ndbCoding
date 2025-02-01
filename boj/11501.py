t=int(input())
import sys
for _ in range(t):
    n=int(sys.stdin.readline())
    li=list(map(int, sys.stdin.readline().split()))
    ans=0
    now_max=li[-1]
    for j in range(len(li)-1, -1, -1):
        if now_max < li[j]:
            now_max=li[j]
        else:
            ans+=now_max-li[j]
    print(ans)
