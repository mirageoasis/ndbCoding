import sys
input = sys.stdin.readline

N = int(input())
chart = list(map(int, input().split()))

# -200000
TOTAL_RNG=200000
visit = [False for i in range(TOTAL_RNG + 1)]

ans=0
for i in range(N):
    for j in range(i):
        target = chart[i] - chart[j] + TOTAL_RNG // 2
        if 0 <= target <= TOTAL_RNG and visit[target]:
            ans+=1
            break

    for j in range(i+1):
        target = chart[i] + chart[j] + TOTAL_RNG // 2
        if 0 <= target <= TOTAL_RNG:
            visit[target] = True

print(ans)