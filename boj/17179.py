import sys
input=sys.stdin.readline

t, m, length = map(int, input().split())

# 1000 * 
# x개 자르기
li=[]
for i in range(m):
    li.append(int(input()))


for i in range(t):
    lim=int(input())
    st=1
    ed=4000001
    ans=-1
    while st < ed:
        # 자르는 최대 길이
        mid=(st+ed)//2
        temp_ans=0
        prev=0
        for j in li:
            if j - prev >= mid:
                temp_ans+=1
                prev=j
        # 마지막 계산
        #print(temp_ans, prev)
        if length - prev >= mid:
            temp_ans+=1
        #print(mid, temp_ans)
        if temp_ans <= lim:
            ed=mid
        else:
            ans=max(mid, ans)
            st=mid+1
    print(ans)

