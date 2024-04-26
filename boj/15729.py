N = int(input())
arr = list(map(int, input().split()))
now = [0 for i in range(N)]

ans=0
for i in range(N):
    if arr[i] != now[i]:
        ans+=1
        for i in range(i, i+3):
            if i < N:
                arr[i] ^=1


print(ans)