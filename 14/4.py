from heapq import heapify, heappop, heappush

# 10 20 30 40 -> 30

# 30 30 40 -> 60

def return_number(li):
    ret = 0
    if len(li) == 1:
        return ret
    heapify(li)

    while len(li) != 1:
        # 둘 뽑아서 길이 1 될 때 까지 실시
        a = heappop(li)
        b = heappop(li)
        ret += (a+b)
        heappush(li, a+b)
        #print(ret)

    return ret



# 60 40 -> 100
li = []
N = int(input())
for i in range(N):
    li.append(int(input()))

print(return_number(li))
