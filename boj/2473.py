from itertools import combinations
from bisect import bisect_left

maxi=(3_000_000_000,3_000_000_000,3_000_000_000)

_=int(input())
chart=list(sorted(map(int, input().split())))

plus_chart=[]
minus_chart=[]

for c in chart:
    if c >= 0:
        plus_chart.append(c)
    else:
        minus_chart.append(c)


if len(plus_chart) > 2:
    if abs(sum(maxi)) > abs(plus_chart[0] + plus_chart[1] + plus_chart[2]):
        maxi=(plus_chart[0], plus_chart[1], plus_chart[2])

if len(minus_chart) > 2:
    if abs(sum(maxi)) > abs(minus_chart[-1] + minus_chart[-2] + minus_chart[-3]):
        maxi=(minus_chart[-3], minus_chart[-2], minus_chart[-1])

if len(plus_chart) >= 2 and len(minus_chart) >= 1:
    for a, b in combinations(plus_chart, r=2):
        res=a+b
        idx=bisect_left(minus_chart, -res)
        if idx > 0:
            if abs(sum(maxi)) > abs(res+minus_chart[idx-1]):
                maxi=(minus_chart[idx-1], a, b)
        if idx < len(minus_chart):
            if abs(sum(maxi)) > abs(res+minus_chart[idx]):
                maxi=(minus_chart[idx], a, b)


if len(minus_chart) >= 2 and len(plus_chart) >= 1:
    for a, b in combinations(minus_chart, r=2):
        res=a+b
        idx=bisect_left(plus_chart, -res)
        if idx > 0:
            if abs(sum(maxi)) > abs(res+plus_chart[idx-1]):
                maxi=(a, b, plus_chart[idx-1])
        if idx < len(plus_chart):
            if abs(sum(maxi)) > abs(res+plus_chart[idx]):
                maxi=(a, b, plus_chart[idx])


print(maxi[0], maxi[1], maxi[2])