#어려운 소인수 분해
import sys
from math import sqrt
N=int(input())

RNG=2237
MAX=5000000
# 

data = list(map(int, sys.stdin.readline().split()))

chart = [i for i in range(MAX+1)]

chart[0] = False
chart[1] = False

def make_chart(chart):
    for i in range(2, RNG):
        if chart[i] == i:
            for j in range(i*i, MAX+1,i):
                if chart[j] == j:
                    chart[j]=i

make_chart(chart)
# for i in range(10):
#     if chart[i]:
#         print(i)

# 46

# 2 3 4 5 6 7 8 9 10 23
# 2 23

# 36

# 2 2 3 3
# 2 2 3 3



for i in data:
    idx = 0
    while i > 1:
        print(chart[i], end=' ')
        i //= chart[i]
    print()