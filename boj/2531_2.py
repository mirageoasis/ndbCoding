import sys
sushi_cnt, kind_cnt, streak_cnt, coupon=map(int, input().split())
sushi=[]
for i in range(sushi_cnt):
    sushi.append(int(sys.stdin.readline()))

start=0
end=streak_cnt

visit=[0 for i in range(kind_cnt+1)]
visit[coupon]+=1
ans=1
now=1
for i in range(end):
    visit[sushi[i]]+=1
    if visit[sushi[i]] == 1:
        now+=1
ans=max(ans, now)
#print(f"now:{now}")

for start in range(1, sushi_cnt):
    # 앞에꺼 빼고
    # 현재 뒤에 있는거 더하기
    prev_sushi=sushi[start-1]
    now_sushi=sushi[(start+streak_cnt-1)%sushi_cnt]
    visit[prev_sushi]-=1
    if visit[prev_sushi] == 0:
        now-=1
    
    visit[now_sushi]+=1
    if visit[now_sushi] == 1:
        now+=1
    #print(f"now: {now}")
    ans=max(ans, now)

print(ans)