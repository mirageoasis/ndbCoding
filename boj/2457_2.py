import sys
n=int(input())

date_chart=[]

month_date=[
    0,  #0
    31, #1
    28, #2
    31, #3
    30, #4
    31, #5
    30, #6
    31, #7
    31, #8
    30, #9
    31, #10
    30, #11
    31
]
# 1월 1일 부터 지난 날짜
def num_to_date(num):
    global month_date
    m=1
    for i in range(1, 13):
        if month_date[i] > num:
            m=i
            break
    return (m, num-month_date[m-1]+1)

def date_to_num(month, date):
    return month_date[month-1]+date-1

for i in range(1, 13):
    month_date[i]+=month_date[i-1]

for i in range(n):
    s_month, s_date, e_month, e_date = map(int, sys.stdin.readline().split())
    s_total_date=date_to_num(s_month, s_date)
    e_total_date=date_to_num(e_month, e_date)
    if e_total_date >= date_to_num(3, 2) and s_month != 12:
        date_chart.append([s_total_date, e_total_date])

date_chart.sort(key=lambda x: (x[0], -x[1]))

#for d in date_chart:
#    print(num_to_date(d[0]), num_to_date(d[1]),end=' ', sep=":")
#print

# 이어질 수 있는 최대 종료일
now_end=date_to_num(3,1)

idx=0
ans=0
while idx < len(date_chart):
    # 여기에서 최대가 될 수 있는 날짜를 찾는다.
    max_end=now_end
    origin_idx=idx
    while idx < len(date_chart):
        #끝이면 break
        idx_start, idx_end = date_chart[idx]
        # 안되는 경우는 위에서 걸린다.
        if now_end < idx_start:
            break
        if now_end<idx_end:
            max_end=max(idx_end, max_end)
        idx+=1
    if idx == origin_idx:
        break
    now_end=max_end
    ans+=1
    if now_end > date_to_num(11,30):
        break


#print(num_to_date(now_end))
print(ans if now_end > date_to_num(11, 30) else 0)

#print(ans)