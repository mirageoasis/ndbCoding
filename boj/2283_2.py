import sys
n, m = map(int, sys.stdin.readline().split())
chart=[]
su=[0 for i in range(1000002)]
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    su[s]+=1
    su[e]-=1

for i in range(1, 1000002):
    su[i]+=su[i-1]
#print(su[:20])
start=0
end=0
s=0
flag=False

while start<=end:
    #print(s, m)
    if s > m:
        s-=su[start]
        start+=1
    elif s < m:
        if end == 1000002:
            break
        s+=su[end]
        end+=1
    else:
        flag=True
        break


if flag:
    print(start, end)
else:
    print(0, 0)