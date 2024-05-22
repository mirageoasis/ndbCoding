# 53분

# 100000 까지 소수 찾아보기

# 만 * 10 * 
K, M = map(int, input().split())

from math import sqrt
from itertools import permutations

LIM=100000
prime_lim=LIM
prime = [True for i in range(prime_lim)]

plus_prime = [False for i in range(LIM+1)]
mul_prime = [False for i in range(LIM+1)]


prime[0]=False
prime[1]=False

for i in range(2, prime_lim):
    if prime[i]:
        for j in range(i*2, prime_lim, i):
            prime[j]=False

prime_set = {idx for idx, val in enumerate(prime) if val}
#print(prime_set)
for i in prime_set:
    for j in prime_set:
        if i != j and i + j <= LIM:
            plus_prime[i+j]=True

for i in prime_set:
    for j in prime_set:
        if i * j <= LIM:
            mul_prime[i*j]=True

## 적립

ans=0

for i in list(permutations('0123456789', K)):
    if i[0] == '0':
        continue
    number = int(''.join(i))

    # M으로 나누기
    # 소수의 곱
    #print(number, diff_prime[number])
    if not plus_prime[number]:
        continue

    while number % M == 0:
        number //= M
    if mul_prime[number]:
        #print(number)
        ans+=1

print(ans)