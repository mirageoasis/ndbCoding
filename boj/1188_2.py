import math

n, m = map(int, input().split())

g=math.gcd(n, m)

n//=g
m//=g
ans=0

if n > m:
    pass
else:
    pass
