# 규칙을 찾아보면 연속해서 증가하는 순열 찾기
# 그러므로 내 앞의 숫자가 몇 인덱스인지 알기
n=int(input())
li=list(map(int, input().split()))

d=dict()
v=[1 for i in range(n+1)]
for i in range(n):
    d[li[i]]=i
maxi=1
for i in range(2, n+1):
    if d[i] > d[i-1]:
        v[i]=v[i-1]+1
        maxi=max(maxi, v[i])

print(n-maxi)