# 다시 풀어보기
import sys
input=sys.stdin.readline

n=int(input())
k=int(input())
li=list(map(int, input().split()))
li.sort()
length=[]
for i in range(len(li)-1):
    length.append(li[i+1]-li[i])
length.sort()
#print(length)
print(sum(length[:n-k]))