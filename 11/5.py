from collections import Counter
from itertools import combinations


N, M = map(int, input().split())
li = map(int, input().split())

cnt=0
#for a, b in l:
#    if a != b:
#        cnt+=1

l = Counter(li)

minus = sum([i * (i - 1) // 2 for i in l.values()])
#print(minus)
print(N * (N - 1) // 2 - minus)
