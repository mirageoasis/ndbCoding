import sys

def translate_into_number(month, day):
    # 일자를 1월 1일부터 지나온 날짜로 변경
    month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_day_sum = sum(month_day[1:month])
    return month_day_sum + day - 1

N = int(input())

temp = []

for i in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    temp.append((translate_into_number(a, b), translate_into_number(c, d) - 1))

temp.sort(key = lambda x : (x[0], -x[1]))

chart = []

for a, b in temp:
    s = translate_into_number(3, 1)
    if b >= s:
        chart.append((a, b))

start_idx=0
ans=0
start_limit=translate_into_number(3, 1)

def index_date_end(idx, chart):
    return chart[idx][1]
flag=False
t = []
now_idx=0
max_idx=0

while True:
    now_idx=start_idx
    max_idx=start_idx

    if now_idx >= len(chart):
        #print(now_idx, len(chart))
        break
    
    # index가 N 이거나, 현재 index의 start가 start_limit의 end보다 크다면 종료
    while now_idx < len(chart) and chart[now_idx][0] <= start_limit:
        # target 보다 끝나는 날이 클 때
        if index_date_end(now_idx, chart) > index_date_end(max_idx, chart):
            max_idx = now_idx
        now_idx+=1
    
    if chart[max_idx][0] > start_limit:
        break

    if index_date_end(max_idx, chart) >= translate_into_number(11, 30):
        #print(index_date_end(max_idx, chart), translate_into_number(11, 30))
        flag = True
        break
    
    if chart[max_idx][0] > start_limit:
        break
    #print(start_idx, now_idx, max_idx, chart, ans, start_limit)
    start_idx = now_idx
    # 시작 end date를 설정
    start_limit=chart[max_idx][1] + 1
    t.append(chart[max_idx])
    ans+=1

#print(t)

if flag:
    print(ans+1)
else:
    print(0)