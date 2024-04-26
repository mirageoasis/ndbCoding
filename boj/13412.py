from math import sqrt, gcd
LIM=int(sqrt(100000001))+1
N=int(input())
'''
2 3 5
2 * 2 * 2 = 8 // 2 = 4

2 
2 // 2 = 1

60060 = 10 * 6006 = 2 3 5 7 11 13
2 * 2 * 2 * 2
'''
def counter(num):
    ans=0
    for i in range(1, int(sqrt(num))+1):
        if num % i == 0:
            first = i
            second = num // i
            if gcd(first, second) == 1:
                ans+=1
    return max(ans, 1)

for i in range(N):
    num=int(input())
    print(counter(num))