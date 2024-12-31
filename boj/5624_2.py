# 2번까지는 허용
# n 번 계산시, 계속 누적합? 비슷하게 수를 확보
n=int(input())
li=list(map(int, input().split()))

chart=[0 for i in range(400001)]

ans=0
for i in range(1, len(li)):
    # chart에 수 추가
    # n번
    flag=False
    for j in range(i):
        s=li[j] + li[i-1] + 200000
        chart[s]+=1
        #print(f"plus {s-200000}, {j} {i-1}")

    # 앞에 수와 더하면서 chart와 비교
    for j in range(i):
        now=li[i] - li[j] + 200000
        if chart[now] != 0:
            #print(now-200000, chart[now])
            flag=True
    
    if flag:
        #print(li[i])
        ans+=1

print(ans)