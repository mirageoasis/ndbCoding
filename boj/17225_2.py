import sys
input=sys.stdin.readline

sang, ji, cnt = map(int, input().split())
li=[]
sang_end=0
ji_end=0
ans=[]
for _ in range(cnt):
    a, b, c = input().split()
    if b == 'B':
        a=int(a)
        c=int(c)
        if sang_end < a:
            sang_end = a
        for i in range(c):
            ans.append([sang_end, 'B'])
            sang_end+=sang
    else:
        a=int(a)
        c=int(c)
        if ji_end < a:
            ji_end = a
        for i in range(c):
            ans.append([ji_end, 'R'])
            ji_end+=ji

ans.sort()
#print(ans)
cnt=1
sang_li=[]
ji_li=[]
for i in range(len(ans)):
    _, alpha = ans[i]
    if alpha == 'B':
        sang_li.append(i+1)
    else:
        ji_li.append(i+1)

print(len(sang_li))
print(*sang_li)

print(len(ji_li))
print(*ji_li)

