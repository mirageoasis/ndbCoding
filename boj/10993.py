N = int(input())

# 1 1, 1
# 2 5 - 4, 3
# 3 13 - 8, 7
# 4 29 - 16, 15

wide = 2**(N+1) - 3
height = 2**N - 1
chart = [[' ' for i in range(wide + 1)] for j in range(height + 1)]

# 반변 2 ** N - 2
# 높이 

# 홀수면 위로
# 짝수면 아래로


def dfs(start_row, start_col, chart, N, real_N):
    # 자신의 2분의 1 지점에서 다른 높이의 dfs 시작
    # 해당 높이는 시작 row + 높이 반
    #print(start_row, start_col)
    if N==1:
        chart[start_row][start_col] = '*'
        return

    now_wide = 2 ** (N+1) - 3
    now_height = 2**N - 1
    # 변 하나 다 그리기
    # 밑이나 위로 가면서 알아서 찍기
    if N % 2 == 0:
        for i in range(now_wide):
            chart[start_row][start_col + i] = '*'
        for i in range(now_height):
            #앞
            chart[start_row + i][start_col + i] = '*'
            #뒤
            chart[start_row + i][start_col + now_wide - 1 - i] = '*'
        dfs(start_row + 1, 2**(real_N) - 2 ** (N - 1) + 1, chart, N - 1, real_N)
    else:
        for i in range(now_wide):
            chart[start_row + now_height - 1][start_col + i] = '*'
        for i in range(now_height):
            #앞
            chart[start_row + now_height - 1 - i][start_col + i] = '*'
            #뒤
            chart[start_row + now_height - 1 - i][start_col + now_wide - 1 - i] = '*'
        dfs(start_row + now_height // 2, 2**(real_N) - 2 ** (N - 1) + 1, chart, N - 1, real_N)


if N != 1:
    dfs(1, 1, chart, N, N)
    for i in range(1, height+1):
        lines =  ''
        for j in range(1, wide+1):
            lines+=chart[i][j]
        #print(list(lines.rstrip()))
        print(lines.rstrip())
else:
    print('*')