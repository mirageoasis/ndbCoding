import sys

n=int(input())
li=[]

for i in range(n):
    li.append(int(sys.stdin.readline()))

#print(li)

maxi=li[0]
ans=0
stack=[li[0]]

for i in li[1:]:
    maxi=max(i, maxi)

    if stack[0] < i:
        ans+=i-stack[0]
        stack.pop()
        stack.append(i)
    else:
        stack.pop()
        stack.append(i)

ans+=(maxi-stack[0])
print(ans)