n, m= map(int, input().split())
li=input().split()
li.sort()

v=['a', 'e', 'o', 'i','u']

from itertools import combinations
#ans=0
for i in combinations(li, n):
    v_count=0
    o_count=0
    for j in i:
        if j in v:
            v_count+=1
        else:
            o_count+=1
    if v_count >= 1 and o_count >= 2:
        print(''.join(i))
        #print(*i)
    
#print(ans)
