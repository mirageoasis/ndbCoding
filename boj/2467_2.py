n=int(input())
li=list(sorted(map(int, input().split())))
start=0
end=len(li)-1
ans=abs(li[start] + li[end])
ans_start=start
ans_end=end
while start != end:
    s=li[start]+li[end]
    # start가 증가
    if abs(s) < ans:
        ans_start=start
        ans_end=end
        ans=abs(s)
    
    if s < 0:
        start+=1
    elif s > 0:
        end-=1
    else:
        break

print((li[ans_start]), li[ans_end])