from heapq import heappush, heappop


N = int(input())

h = []

cnt = 0
num = 1
heappush(h, 1)
li = []
li.append(0)

while cnt < N:
    num = heappop(h) 
    if num == li[-1]:
        continue
    #print(num)
    heappush(h, num*2)
    heappush(h, num*3)
    heappush(h, num*5)
    cnt+=1

print(num)