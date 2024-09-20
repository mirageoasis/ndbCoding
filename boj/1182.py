from itertools import product

N, S = map(int, input().split())
chart=list(map(int, input().split()))
ans=0


for arr in product([True, False], repeat=N):
    if not arr.count(True):
        continue
    temp=0
    for a, c in zip(arr, chart):
        if a == True:
            temp+=c
    
    if temp == S:
        ans+=1


print(ans)