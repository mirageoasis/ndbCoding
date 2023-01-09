N=int(input())
li=list(map(int, input().split()))
lis=[0] * N
lis[0] = li[0]
lis[1] = li[1]

for i in range(2, N):
    lis[i] = max(lis[i - 1], lis[i - 2] + li[i])

print(lis[N - 1])