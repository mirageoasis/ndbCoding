import sys
n=int(input())

start_chart=[]
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
        if s_total_date < date_to_num(3, 1):
            start_chart.append([s_total_date, e_total_date])
        else:
            date_chart.append([s_total_date, e_total_date])

start_chart.sort(key=lambda x:(-x[1]))
date_chart.sort(key=lambda x: (x[0], -x[1]))


