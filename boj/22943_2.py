from itertools import permutations
k, m=map(int, input().split())
# 5자리니까 ㄱㅊ을 듯?
LIM=100000
is_prime=[True for i in range(LIM)]

is_prime[0]=False
is_prime[1]=False
for i in range(2, LIM):
    if is_prime[i]:
        for j in range(i*2, LIM, i):
            is_prime[j]=False
prime_list=[]
#9P5 -> 
for i in range(LIM):
    if is_prime[i]:
        prime_list.append(i)

ans_set=set()
plus_set=set()
for i in range(len(prime_list)):
    for j in range(i, len(prime_list)):
        if i != j and prime_list[i]+prime_list[j] < LIM:
            plus_set.add(prime_list[i]+prime_list[j])
        if prime_list[i]*prime_list[j] < LIM:
            ans_set.add(prime_list[i]*prime_list[j])

ans=0
for i in permutations([1,2,3,4,5,6,7,8,9,0], r=k):
    if i[0] == 0:
        continue

    number=sum([10**(k-idx-1) * val for idx, val in enumerate(i)])
    if not (number in plus_set):
        continue

    while number % m == 0:
        number //=m
    if number in ans_set:
        ans+=1

print(ans)