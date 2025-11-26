# 차피 10번 이내

n=int(input())
result=list(map(int, input().split()))
real_lim=1
while True:
    if 2**(real_lim+1) > n:
        break
    real_lim+=1
from collections import deque
for first in range(1, real_lim+1):
    first_start=deque([i for i in range(1, n+1)])
    # 처음에는 n개 그대로 실험하기
    prev_up=n
    
    for first_step in range(first, -1, -1):
        filter_cnt=2**first_step
        new_li=deque()

        # 앞의 원소 구출
        for _ in range(prev_up):
            new_li.append(first_start.popleft())
        # 필요한 것만 뒤에서 추출
        # new_li_2에는 추출한
        filter_li=deque()
        for _ in range(filter_cnt):
            filter_li.appendleft(new_li.pop())
        # new_li에서 
        while new_li:
            first_start.appendleft(new_li.pop())
        while filter_li:
            first_start.appendleft(filter_li.pop())
        prev_up=filter_cnt
    #print(first_start)
    for second in range(1, real_lim+1):
        # 첫번째에서 실험한거 받아오기
        second_start=deque(list(first_start)[:])
        prev_up=n
        
        for second_step in range(second, -1, -1):
            #print(second_start, prev_up)
            filter_cnt=2**second_step
            new_li=deque()

            # 앞의 원소 구출
            for _ in range(prev_up):
                #print(second_start, prev_up, _)
                new_li.append(second_start.popleft())
            # 필요한 것만 뒤에서 추출
            # new_li_2에는 추출한
            #print(new_li, filter_cnt)
            filter_li=deque()
            for _ in range(filter_cnt):
                filter_li.appendleft(new_li.pop())
            # new_li에서 
            while new_li:
                second_start.appendleft(new_li.pop())
            while filter_li:
                second_start.appendleft(filter_li.pop())
            prev_up=filter_cnt
        
        #print(second_start)
        #print()
        # 결과 판독
        #print(first, second)
        for i in range(n):
            if second_start[i] != result[i]:
                break
        else:
            print(first, second)
            exit(0)


    