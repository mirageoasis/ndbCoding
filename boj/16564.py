# 21분 시작
import sys
from collections import deque

N, K = map(int, input().split())
chart = []

for i in range(N):
    chart.append(int(sys.stdin.readline()))

# 가장 레벨 작은 얘를 support
# K는 탄창
chart.sort()
que = deque(chart)

flag = que.popleft()
cnt=1
if que:
    while que:
        head=que[0]
        tail=que[-1]
        if K > (head-flag)*cnt:
            if head == tail:
                to_add=(head-flag)
                if K > to_add * cnt:
                    flag=head
                    K-=(to_add * cnt)
                    flag+=(K//len(chart))
                else:
                    print("hi")
                    flag+=K//cnt
                break
            K-=(head-flag)*cnt
        else:
            flag+=(K)//cnt
            break
        cnt+=1
        flag=que.popleft()
    print(flag)
else:
    print(flag+K)

#print(que)