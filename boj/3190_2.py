import sys
from collections import deque

board_length=int(input())
apple_num=int(input())
apple_cord=set()
snake=deque()
snake.append((0, 0))
dir_dict={
    0: [-1, 0],
    1: [0, -1],
    2: [1, 0],
    3: [0, 1],
}
direction_num=3
order_dict=dict()
for _ in range(apple_num):
    first, second = map(int, sys.stdin.readline().split())
    apple_cord.add((first-1, second-1))
order_num=int(input())

for _ in range(order_num):
    a, b = sys.stdin.readline().split()
    order_dict[int(a)]=b
tick=1

while True:
    # direction 만큼 머리 움직이기
    row, col = snake[0]
    # 새로운 row, col
    new_row=row + dir_dict[direction_num][0] 
    new_col=col + dir_dict[direction_num][1] 
    # 범위 바깥이면 out
    if not (0<=new_row<board_length and 0<=new_col<board_length):
        break
    # 뱀의 몸체가 있다면
    snake_set=set(snake)
    if (new_row, new_col) in snake_set:
        break
    
    # 새로운 점에 사과가 있으먄
    if (new_row, new_col) in apple_cord:
        apple_cord.remove((new_row, new_col))
        snake.appendleft((new_row, new_col))
    # 사과 없다면
    else:
        snake.appendleft((new_row, new_col))
        snake.pop()
    #print(snake)

    # 만약에 해당하는 방향 전환 있으면 실행하기
    if tick in order_dict:
        if order_dict[tick] == 'L':
            direction_num+=1
            direction_num%=4
        else:
            direction_num+=3
            direction_num%=4
    tick+=1

print(tick)