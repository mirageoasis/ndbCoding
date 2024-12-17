n, m = map(int, input().split())
li=list(map(int, input().split()))

# 일단 부분합?인가 가능할까 싶다가도 0.5초기 때문에 1만 * 1만 -> 억 이라서 안됨
# 그래서 투포인터
# 수의 합이 연속이기 때문에 적용 가능함

start=0
end=0
s=0
ans=0
# 합은 [start, end)까지
while True:
    
    if s < m:
        if end == len(li):
            break
        
        s+=li[end]
        end+=1
    else:
        if s == m:
            ans+=1
        s-=li[start]
        start+=1

print(ans)