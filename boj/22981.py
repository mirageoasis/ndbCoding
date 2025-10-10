n, k = map(int, input().split())
li=list(map(int, input().split()))

li.sort()
# 전부 값을 알고 하기
mini=10**19
from math import ceil
from decimal import Decimal
for i in range(1, n):
    first=li[0]
    pivot=li[i]
    # 0~i) [i, n)
    first_sum = first * (i)
    second_sum = pivot * (n - i)
    mini=min(mini, ceil(Decimal(k) / Decimal(first_sum + second_sum)))

print(mini)