# 9시 50분 시작
from heapq import heapify, heappush, heappop

N, M = map(int, input().split())
base = list(map(int, input().split()))
add = list(map(int, input().split()))

# 파이썬은 최소힙만 가능하기 때문에 add는 음수 처리를 한다.

heap = [[-j, i] for i, j in zip(base, add)]

# heap 만들기
heapify(heap)

cnt=0
ans=0

while cnt < N * 24:
    adder, now_score = heappop(heap)
    adder = abs(adder)
    
    if adder == 0:
        break

    # cnt 흐르는 만큼
    quota = (100 - now_score) // adder
    left = (100 - now_score) % adder

    #지나갈 시간
    to_elapse = min(quota, N * 24 - cnt)
    heappush(heap, [-left, now_score+to_elapse * adder])
    ans+=adder * to_elapse
    cnt+=to_elapse

print(ans+sum(base))





