import sys
input=sys.stdin.readline
n, m = map(int, input().split())

li=[]

for i in range(n):
    li.append(int(input()))

start=max(li)
end=10000 * 100000 + 1

while start<end:
    mid=(start+end)//2
    budget=0
    temp=0
    for i in li:
        if budget < i:
            budget=mid
            temp+=1
        budget-=i
    #print(temp, )
    if temp <= m:
        end=mid
    else:
        start=mid+1

print(start)