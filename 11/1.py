N=int(input())
li=list(map(int, input().split()))

li.sort()

minus=0
cnt=0

for idx, elem in enumerate(li):
    if elem <= idx + 1 - minus:
        minus=idx+1
        cnt+=1
print(cnt)