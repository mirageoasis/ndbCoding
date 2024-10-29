#37분 시작
from collections import deque

N, bridge_len, weight = map(int, input().split())

chart=list(map(int, input().split()))

end_que=deque()
middle_que=deque([0 for i in range(bridge_len)])
start_que=deque(chart)
middle_weight=0

while middle_que or start_que:
    temp2=middle_que.popleft()
    middle_weight-=temp2
    end_que.append(temp2)
    
    if start_que:
        temp=start_que[0]
        if middle_weight + temp <= weight:
            middle_que.append(start_que.popleft())
            middle_weight+=temp
        else:
            middle_que.append(0)
    
    #print(start_que)
    #print(middle_que)
    #print(end_que)
    #print()


print(len(end_que))