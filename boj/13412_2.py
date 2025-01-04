import math

t=int(input())



for _ in range(t):
    num=int(input())
    new_num=num
    if num == 1:
        print(1)
        continue
    ans=0
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            first=i
            second=num//i
            if math.gcd(first, second) == 1:
                ans+=1
    print(ans)