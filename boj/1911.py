#이거도 역시 부분합 ㄴㄴ
import sys
import math
n, m = map(int, input().split())
chart=[]
for i in range(n):
    chart.append(list(map(int, sys.stdin.readline().split())))
#print(chart)
# 출발점을 기준으로 나눠준다.
chart.sort(key=lambda x: x[0])

now_idx=0
ans=0
while now_idx < len(chart):
    now_start, now_end = chart[now_idx]
    now_end-=1
    # 마지막 점에서 
    length=now_end-now_start+1
    # 이번 널빤지가 끝을 향할 곳
    board_cnt=math.ceil(length/m)
    ans+=board_cnt
    now_end = board_cnt * m + now_start-1
    #print("now_end",now_start, now_end)
    now_idx+=1
    while now_idx < len(chart):
        #print(now_idx, chart[now_idx], now_end, chart[now_idx][1]-now_end)
        new_start, new_end = chart[now_idx]
        new_end-=1
        # 뒤의 start가 now_end보다 크면 계산 시작
        # 더하고 뒤에 오는거 계산 + 1처리하는거
        if new_start > now_end:
            #print("break")
            break
        now_end+=1
        new_length=new_end-now_end+1
        board_cnt=math.ceil(new_length/m)
        ans+=board_cnt
        #print("board_cnt ", board_cnt)
        now_end=board_cnt*m+now_end-1
        #print("now_end",now_start, now_end)
        now_idx+=1
    
print(ans)