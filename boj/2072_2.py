n=int(input())

chart=[[-1 for i in range(19)]for j in range(19)]

def mov(start_row, start_col, row_dir, col_dir):
    global chart
    start_num=chart[start_row][start_col]
    cnt=0
    while True:
        start_row+=row_dir
        start_col+=col_dir
        if (not 0<=start_row<19) or (not 0<=start_col<19):
            break
        if not (chart[start_row][start_col] == start_num):
            return cnt
        cnt+=1
    return cnt

for i in range(n):
    now_row, now_col = map(int, input().split())

    now_row-=1
    now_col-=1
    chart[now_row][now_col]=i%2

    # 가로
    first=mov(now_row, now_col, 0, 1)
    second=mov(now_row, now_col, 0, -1)

    if first + second == 4:
        print(i+1)
        break

    # 세로
    first=mov(now_row, now_col, 1, 0)
    second=mov(now_row, now_col, -1, 0)

    if first + second == 4:
        print(i+1)
        break

    # 대각선 1
    first=mov(now_row, now_col, 1, 1)
    second=mov(now_row, now_col, -1, -1)

    if first + second == 4:
        print(i+1)
        break

    # 대각선 2
    first=mov(now_row, now_col, -1, 1)
    second=mov(now_row, now_col, 1, -1)

    if first + second == 4:
        print(i+1)
        break
else:
    print(-1)