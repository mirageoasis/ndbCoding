import sys

input=sys.stdin.readline

n=int(input())
l=int(input())
li=list(sorted(list(set(map(int, input().split())))))
cr=[]

for i in range(len(li)-1):
    cr.append(li[i+1]-li[i])
cr.sort(reverse=True)

print(sum(cr[l-1:]))