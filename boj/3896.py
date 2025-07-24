import sys
n=int(input())
INF=1299710
is_prime = [True for i in range(INF)]

is_prime[0]=False
is_prime[1]=False

for i in range(2, INF):
    for j in range(i * 2, INF, i):
        is_prime[j]=False
prime_list=[]
for i in range(2, INF):
    if is_prime[i]:
        prime_list.append(i)
prime_reversed=list(reversed(prime_list))

def lower_bound(target):
    global prime_reversed
    start=0
    end=len(prime_reversed)
    while end > start:
        mid=(end+start)//2
        if prime_reversed[mid] > target:
            start=mid+1
        else:
            end=mid                
    return prime_reversed[start]

def upper_bound(target):
    global prime_list
    start=0
    end=len(prime_list)
    while end > start:
        mid=(end+start)//2
        if prime_list[mid] <= target:
            start=mid+1
        else:
            end=mid
    return prime_list[start]


for i in range(n):
    num=int(sys.stdin.readline())
    if is_prime[num]:
        print(0)
    else:
        #print(upper_bound(num))
        #print(lower_bound(num))
        print(upper_bound(num) - lower_bound(num))


