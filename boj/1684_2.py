import math
math.gcd
n=input()
li=list(map(int, input().split()))

li.sort()
t=[]

for i in range(0, len(li) - 1):
    t.append(li[i+1] - li[i])


def gcd(a, b):
    small=min(a, b)
    big=max(a, b)

    while small != 0:
        n=big%small
        big=small
        small=n
    return big

while len(t) > 1:
    temp_t=[]
    for i in range(0, len(t) - 1):
        temp_t.append(gcd(t[i+1], t[i]))

    t=temp_t

print(t[0])