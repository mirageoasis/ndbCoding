from math import gcd
from functools import reduce

t=int(input())

mother = []
son = []
son_mul = []

for i in range(t):
    n, m = map(int, input().split())
    son.append(n)
    mother.append(m)
    # 분모를 다 곱하고 

all_mul = reduce(lambda x, y : x * y, mother)

for m, s in zip(mother, son):
    son_mul.append(s * all_mul // m)

son_gcd = gcd(*son_mul) 
ans_son = son_gcd // gcd(son_gcd, all_mul)
ans_mom = all_mul // gcd(son_gcd, all_mul)

print(ans_son, ans_mom)