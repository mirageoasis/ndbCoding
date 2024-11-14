import sys

n, k, b = map(int, input().split())
chart=[True for i in range(n+1)]

for i in range(b):
    num = int(sys.stdin.readline())
    chart[num]=False

cnt=0
for i in range(1, k+1):
    if chart[i]:
        cnt+=1
ans=k-cnt

for i in range(2, n+2-k):
    # i - 1 빼고
    # i + k - 1 는 더한다.

    if chart[i-1]:
        cnt-=1

    if chart[i+k-1]:
        cnt+=1
    #print(cnt)
    ans=min(ans, k-cnt)

print(ans)