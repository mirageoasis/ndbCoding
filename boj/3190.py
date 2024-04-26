from collections import deque

# 10000 * 100
# list 하나로 퉁치기 -> 가능할꺼 같음
# queue하나와 뱀의 원소 set을 사용해서 하기

N = int(input())
K = int(input())

direction_dict = {
    (0, 1) : {
        "L" : (-1, 0),
        "D" : (1, 0),
    },
    (0, -1) : {
        "L" : (1, 0),
        "D" : (-1, 0),
    },
    (1, 0) : {
        "L" : (0, 1),
        "D" : (0, -1),
    },
    (-1, 0) : {
        "L" : (0, -1),
        "D" : (0, 1),
    },
}

command_dict = dict()

apple_loc = set()

for i in range(K):
    apple_loc.add(tuple(map(int, input().split())))

L = int(input())

# queue로 뱀을 만들기

snake_queue = deque()
snake_set = set()
ans = 1
now_pos = (0, 1)

for i in range(L):
    a, b = input().split()
    command_dict[int(a)] = b

snake_queue.appendleft((1, 1))
snake_set.add((1, 1))

while True:
    # 1. 뱀의 머리가 이동을 함
    # 2 머리 좌표를 queue에 추가하지 않음
    # 2 - 1 사과가 존재
    # 꼬리를 냅둔다. apple_loc에서 사과 제외
    # 2 - 2 사과가 없음
    # 꼬리를 냅두지 않는다. -> queue에서 재명 및 set에서 제거
    # 3. 머리의 위치가 올바른지 확인
    # 머리가 판을 벗어나면 out! 아니면 set에 머리가 들어갈 곳이 존재하는지 확인    

    # 이후에 좌표를 변환하기
    row_dir, col_dir = now_pos

    future_row = snake_queue[0][0] + row_dir
    future_col = snake_queue[0][1] + col_dir

    future_loc = (future_row, future_col)

    if future_loc in snake_set:
        break

    if future_loc in apple_loc:
        apple_loc.remove(future_loc)
    else:
        snake_set.remove(snake_queue.pop())

    # 조건
    
    if future_row > N or future_row < 1 or future_col > N or future_col < 1:
        break
    
    #print(snake_queue, future_loc, ans, now_pos)

    snake_set.add(future_loc)
    snake_queue.appendleft(future_loc)

    # 좌표 변환
    if ans in command_dict:
        # 좌표 변환
        now_pos = direction_dict[now_pos][command_dict[ans]]
    ans+=1


print(ans)