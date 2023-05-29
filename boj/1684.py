from math import gcd
# 하... python gcd


N=int(input())

# def gcd(a, b):
#     c = max(a, b)
#     d = min(a, b)

#     while True:
#         if c % d != 0:
#             temp = c % d
#             c = d
#             d = temp
#         else:
#             break
    
#     return d
    
li=list(map(int, input().split()))
new_li = []
li.sort()

for i in range(N-1):
    new_li.append(li[i+1] - li[i])

new_li = [x for x in new_li if x != 0]

#ans=new_li[0]

# python에는 gcd가 있다.. python의 그의 한계는 어디까지인가?
# 파이썬 펀치! 파이썬 펀치! 파이썬 펀치! 파이썬 펀치! 그는 신이야!


ans = gcd(*new_li)

# for i in new_li:
#     ans = gcd(i, ans)
print(ans)