# 큐 대로 계산하고 x초 블라블라
from collections import deque
import sys

wait_que=deque()

wait_cnt, time_limit, problem_time = map(int, input().split())

for i in range(wait_cnt):
    # num, time
    wait_que.append(tuple(map(int, sys.stdin.readline().split())))

#print(wait_que)

after_cnt=int(input())
after_dict=dict()


for i in range(after_cnt):
    # number t c
    p, t, c = map(int, sys.stdin.readline().split())
    after_dict[c]=(p, t)

now_time=0
while now_time < problem_time:
    customer_id, customer_time = wait_que.popleft()
    #print(f"{customer_id}, {customer_time}")
    need_time = min(customer_time, time_limit)
    temp_time=0
    while temp_time < need_time and now_time < problem_time:
        customer_time-=1
        print(customer_id)
        now_time+=1
        temp_time+=1
        if now_time in after_dict:
            wait_que.append(after_dict[now_time])
        #print(wait_que)
    # 처리하고 담아주기
    if customer_time > 0:
        wait_que.append((customer_id, customer_time))