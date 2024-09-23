from itertools import combinations
from bisect import bisect_left, bisect_right
from math import comb

N=int(input())
chart=list(map(int, input().split()))

minus=[i for i in chart if i < 0]
plus=[i for i in chart if i >= 0]

minus.sort()
plus.sort()

# 양수 2개 음수 1개
ans=0

for first, second in combinations(minus, 2):
    idx = bisect_left(plus, abs(first+second))
    start_idx = bisect_left(plus, abs(first+second))
    end_idx=bisect_right(plus, abs(first+second))
    ans+=(end_idx-start_idx)

for first, second in combinations(plus, 2):    
    start_idx = bisect_left(minus, -first-second)
    end_idx=bisect_right(minus, -first-second)
    ans+=(end_idx-start_idx)

zero=plus.count(0)

#print(len(list(combinations([0], 3))))

ans+=comb(zero, 3)

print(ans)

# 000 거르기

# 음수 2개 양수 1개