"""
날도 크고 과목 개수도 시간 복잡도가 너무 크다.
"""
from collections import deque
from heapq import heappop, heappush
day_num, class_num = map(int, input().split())

start_score=list(map(int, input().split()))
per_score=list(map(int, input().split()))
heap=[]

for i in range(class_num):
    heappush(heap, (-per_score[i],start_score[i]))

left_time=day_num*24
total_score=0

while heap and left_time:
    p_s, now_score = heappop(heap)
    p_s=abs(p_s)

    can_time=(100 - now_score) // p_s
    minus_time=min(left_time, can_time)


    # 정산
    now_score+=minus_time*p_s
    left_time-=minus_time

    if now_score == 100:
        total_score+=100
    elif now_score < 100:
        heappush(heap, (-(100-now_score), now_score))

for _, score in heap:
    total_score+=score

print(total_score)