# 4시 09분
from itertools import combinations

N, M = map(int, input().split())

chart=input().split()
chart.sort()

# 다 고려하고 한개의 모음도 없는 경우
# 한개의 자음만 있는 경우
# 0개의 자음만 있는 경우

vol={'a', 'e', 'o', 'i', 'u'}

for i in combinations(chart, r=N):
    vol_cnt=0
    el_cnt=0
    for j in i:
        if j not in vol:
            el_cnt+=1
        else:
            vol_cnt+=1
    
    if el_cnt >= 2 and vol_cnt >= 1:
        print(''.join(i))