N = int(input())

game = []

chart = [[-1 for i in  range(20)] for j in range(20)]

for i in range(N):
    game.append(list(map(int, input().split(' '))))


def streak_cnt(i, color, fin_cnt, chart):
    move = (
        ((0, -1), (0, 1)),
        ((-1, 0), (1, 0)),
        ((1, -1), (-1, 1)),
        ((-1, -1), (1, 1))
    )
    
    row = i[0]
    col = i[1]

    for first, second in move:
        streak_temp = 1
        
        row_direction = first[0]
        col_direction = first[1]
        now_row = row
        now_col = col
        while True:    
            now_row += row_direction
            now_col += col_direction

            if 0 < now_row <= 19 and 0 < now_col <= 19 and chart[now_row][now_col] == color:
                streak_temp+=1
            else:
                break
        row_direction = second[0]
        col_direction = second[1]
        now_row = row
        now_col = col
        while True:
            now_row += row_direction
            now_col += col_direction
            if 0 < now_row <= 19 and 0 < now_col <= 19 and chart[now_row][now_col] == color:
                streak_temp+=1
            else:
                break

        if streak_temp == fin_cnt:
            return True

    return False


for idx, i in enumerate(game):
    # 0
    # 1
    color = idx % 2
    chart[i[0]][i[1]] = color
    if streak_cnt(i, color, 5, chart):
        print(idx+1)
        break
else:
    print(-1)