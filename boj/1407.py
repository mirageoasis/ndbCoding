import math
# 2^n으로 나눴을 때 안나눠지면 2^n-1으로 나눠지는 최대경우

a, b = map(int, input().split())

def cal(num):
    origin=num
    div=2
    ret=0
    while num:
        p=math.ceil(num/2)
        ret+=p * (div//2)
        num-=p
        div*=2
    return ret

print(cal(b) - cal(a-1))