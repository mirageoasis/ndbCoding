# 19시 06분
from heapq import heappush, heappop, heapify

gift_len, child_len = map(int, input().split())

# navie하게 하면 10 ^ 10승 
# 100억 ^^ 
# heap 사용하면 -> 5 * 3 * 10 ^ 5 

gift=list(map(int, input().split()))
child=list(map(int, input().split()))

gift=[-i for i in gift]

heapify(gift)
flag=1
for c in child:
    elem=abs(heappop(gift))
    
    
    if elem < c:
        flag=0
        break
    else:
        heappush(gift, -(elem - c))

print(flag)
