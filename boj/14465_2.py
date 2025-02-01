import sys
n, k, b = map(int, input().split())
li=[]

visit=[True for i in range(n+1)]

for i in range(b):
    visit[int(sys.stdin.readline())]=False

start=1
end=k
s=0
ans=9999999
for i in range(1, k+1):
    if visit[i]:
        s+=1
ans=k-s
#print(f"ans:{ans}")
for i in range(2, n):
    start=i
    end=i+k-1
    if end == n+1:
        break
    if visit[start-1]:
        s-=1
    if visit[end]:
        s+=1
    ans=min(ans, k-s)
    #print(f"ans:{ans}")

print(ans)
