import sys
import heapq

n=int(input())
li=list(map(int, input().split()))
li.insert(0, 0)

chart=[[] for i in range(6)]

for i in range(n):
    diffi, time = map(int, sys.stdin.readline().split())
    chart[diffi].append(time)
# 그냥 구현해도 상관 없을 듯, 모든 입력을 받고 나서 계산이 가능함. 게산을 동적으로 할 필요가 없음

ans=0
for difficult in range(1, 6):
    limit = li[difficult]
    # 정렬한다.
    now=chart[difficult]
    now.sort()
    prev=now[0]
    for i in range(limit):
        ans+=now[i]
        ans+=now[i]-prev
        prev=now[i]
    #print(ans)

print(ans+240)