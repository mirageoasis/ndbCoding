def two_cnt(num):
    cnt=0
    while num%2 == 0:
        num//=2
        cnt+=1
    return cnt

def three_cnt(num):
    cnt=0
    while num%3 == 0:
        num//=3
        cnt+=1
    return cnt

n=int(input())
li=list(map(int, input().split()))
ans=[]

for i in li:
    ans.append((i, two_cnt(i), three_cnt(i)))

ans.sort(key=lambda x: (-x[2], x[1]))

for a in ans:
    print(a[0], end=' ')

print()