# 4시 49분
import math

now_num, add_num, max_len = map(int, input().split())

chart=list(map(int, input().split()))
dis=[]

chart.insert(0, 0)
chart.append(max_len)
chart.sort()

#print(chart)

for i in range(0, len(chart)-1):
    dis.append(chart[i+1]-chart[i])
dis.sort()
#print(dis)
for diff in range(1, 1000):
    su=sum([math.ceil(d/diff)-1 for d in dis])
    
    if su <= add_num:
        print(diff)
        break