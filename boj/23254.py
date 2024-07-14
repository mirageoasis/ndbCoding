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

"""
다른 풀이법으로는
0~100 범위를 가지는 cnt라는 배열을 만들고
지금 점수 0, 덧셈 점수 33 일 때
while문을 수행하면서 
덧셈 점수에 해당하는 index에 1을 올리고 -> 33을 3번 더할 수 있으니 33에 3을 더함
마지막에는 1밖에 더할 수 없기 때문에 1에 1을 더해준다.

그리고 cnt 배열의 100부터 거꾸로 세면서 가장 큰 원소들을 더해준다.
"""




