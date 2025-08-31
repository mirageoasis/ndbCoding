n, m, r = map(int, input().split())

chart=[]

for _ in range(n):
    chart.append(list(map(int, input().split())))

high_left=[0, 0]
low_left=[n-1, 0]

high_right=[0, m-1]
low_right=[n-1, m-1]
loop=min(m, n) // 2
from collections import deque
while loop:
    buffer=deque()
    for row in range(high_left[0], low_left[0]):
        buffer.append(chart[row][high_left[1]])    
    for col in range(low_left[1], low_right[1]):
        buffer.append(chart[low_left[0]][col])
    for row in range(low_right[0], high_right[0], -1):
        buffer.append(chart[row][low_right[1]])
    for col in range(high_right[1], high_left[1], -1):
        buffer.append(chart[high_right[0]][col])
    #print(buffer)
    for i in range(r):
        buffer.appendleft(buffer.pop())

    cnt=0
    for row in range(high_left[0], low_left[0]):
        chart[row][high_left[1]]=buffer[cnt]
        cnt+=1
    for col in range(low_left[1], low_right[1]):
        chart[low_left[0]][col]=buffer[cnt]
        cnt+=1
    for row in range(low_right[0], high_right[0], -1):
        chart[row][low_right[1]]=buffer[cnt]
        cnt+=1
    for col in range(high_right[1], high_left[1], -1):
        chart[high_right[0]][col]=buffer[cnt]
        cnt+=1
    
    high_left=[high_left[0]+1, high_left[1]+1]
    low_left=[low_left[0]-1, low_left[1]+1]
    high_right=[high_right[0]+1, high_right[1]-1]
    low_right=[low_right[0]-1, low_right[1]-1]
    loop-=1

for c in chart:
    print(*c)

