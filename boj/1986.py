from collections import deque    
from itertools import chain
from collections import Counter

n, m = map(int, input().split())

def bfs(n, m, start_row, start_col, safe_chart, chart):
    que = deque()
    # 8방향

    que.append((1, 0, 1))
    que.append((-1, 0, 1))
    que.append((0, 1, 1))
    que.append((0, -1, 1))
    
    que.append((1, 1, 1))
    que.append((1, -1, 1))
    que.append((-1, 1, 1))
    que.append((-1, -1, 1))


    while que:
        row_to_mv, col_to_mv, cnt = que.popleft()

        dest_row = start_row + row_to_mv * cnt
        dest_col = start_col + col_to_mv * cnt
        if 0<=dest_row<n and 0<=dest_col<m and not chart[dest_row][dest_col]:
            #print(dest_row, dest_col, chart[dest_row][dest_col])
            safe_chart[dest_row][dest_col] = False
            que.append((row_to_mv , col_to_mv, cnt+1))

queen_list = list(map(int, input().split()))
knight_list = list(map(int, input().split()))
pawn_list = list(map(int, input().split()))

queen_list = queen_list[1:]
knight_list = knight_list[1:]
pawn_list = pawn_list[1:]

queen_list = [
    (queen_list[i*2] - 1, queen_list[i*2+1] - 1) for i in range(len(queen_list) // 2)
]if queen_list else []
knight_list = [
    (knight_list[i*2] - 1, knight_list[i*2+1] - 1) for i in range(len(knight_list) // 2)
]if knight_list else []
pawn_list =  [
    (pawn_list[i*2] - 1, pawn_list[i*2+1] - 1) for i in range(len(pawn_list) // 2)
] if pawn_list else []

# print(queen_list)
# print(pawn_list)
# print(knight_list)

# 100개
safe_chart = [[True for i in range(m)] for j in range(n)]
# 말이 있으면 1 없으면 0
chart = [[0 for i in range(m)] for j in range(n)]

for row, col in pawn_list:
    chart[row][col] = 1
    safe_chart[row][col] = False

# 각각 순회 완료
for row, col in knight_list:
    chart[row][col] = 1
    safe_chart[row][col] = False
    d_r = [-1,-2,-2,-1,2,1,1,2]
    d_c = [-2,-1,1,2,-1,-2,2,1]

    for i in range(8):
        new_row = row + d_r[i]
        new_col = col + d_c[i]

        if 0<=new_row<n and 0<=new_col<m:
            safe_chart[new_row][new_col] = False

for row, col in queen_list:
    chart[row][col] = 1
    safe_chart[row][col] = False
    bfs(n, m, row, col, safe_chart, chart)

# for c in safe_chart:
#     print(c)
# print()
# for c in chart:
#     print(c)
# print()
# for c in safe_chart:
#     print(c)
# for c in chart:
#     print(c)
# print()


print(Counter(chain(*safe_chart))[True])