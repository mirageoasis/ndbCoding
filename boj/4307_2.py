t=int(input())
import sys
for _ in range(t):
    n, m = map(int, input().split())
    ans_small=0
    ans_big=0

    for i in range(m):
        k = int(sys.stdin.readline())
        a,b=n-k, k
        a, b = min(a, b), max(a, b)
        ans_small=max(ans_small, a)
        ans_big=max(ans_big, b)
    
    print(ans_small, ans_big)