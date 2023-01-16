from collections import deque
'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''

N=int(input())
K=int(input())
apple_cord=set()
for _ in range(K):
    a, b = map(int, input().split())
    apple_cord.add((a, b))

#print(apple_cord)

L=int(input())
move=dict()
# x 초 후에 방향 전환
for _ in range(L):
    a, b = input().split()
    move[int(a)]=b


# apple cord 를 dictionary 로 만든다.
# 이동할 때 마다 apple cord에서 좌표 확인 만약에 값이 1이면 뱀
# 뱀은 deque를 사x용해서 구현

snake_queue = deque()


answer=0
d_r = [0, -1, 0, 1]
d_c = [1, 0, -1, 0]
row=0
col=0
direction_idx=0

import time

while True:

    # 해당 시간에 움직임이 존재하는지
    if move.get(answer): # 0이랑 1이 뜨지 않는다.
        direction = move.get(answer)
        if direction == "L":
            direction_idx+=1
            direction_idx%=4
        elif direction == "D":
            direction_idx+=3
            direction_idx%=4
    
    # 시간의 움직임대로 이동해준다.
    row+=d_r[direction_idx]
    col+=d_c[direction_idx]

    # 좌표에서 벗어났는지    
    if row < 0 or row > N or col < 0 or col > N:
        print("world border!")
        break

    # 사과인지
    apple_flag=False

    if (row, col) in apple_cord:
        apple_flag=True
        apple_cord.remove((row, col))
    
    
    # 또한 뱀을 줄일지 말지 고민
    
    if (row, col) in snake_queue:
        print("exited with suicide")
        break
    
    # 새로운 곳의 좌표를 추가한다.
    snake_queue.append((row, col))

    if not apple_flag:
        snake_queue.popleft()
    
    answer+=1
    #print(answer, (row, col))
    #time.sleep(0.3)

print(f'{answer}')