import sys
N, M = map(int, input().split())

chart=[]

for i in range(N):
    chart.append(int(sys.stdin.readline()))
chart.sort()

# 1 이랑 5는 비교할 필요가 없음

start=0
end=0
now=0
ans=2_000_000_001

while True:
    if start == N or end == N:
        break
    now=chart[end]-chart[start]
    if now > M:
        start+=1
    else:
        end+=1
    #print(chart[start:end+1])
    if now >= M:
        ans=min(ans, now)
    
print(ans)