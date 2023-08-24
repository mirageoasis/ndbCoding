N=int(input())

chart = []

for i in range(N):
    chart.append(list(input()))


# 8가지 방향

dic = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, -1),
    (1, 1),
    (-1, -1),
    (-1, 1),
]

def range_check(loc):
    row, col = loc
    return 0 <= row <= N - 1 and 0 <= col <= N - 1

ans = -1

for i in range(N):
    for j in range(N):
        if chart[i][j] == '.':
            continue
        
        for k in range(8):
            row, col = dic[k]
            one_dir = (i + row, j + col)
            two_dir = (i + row * 2, j + col * 2)

            if not range_check(one_dir):
                continue
            if not range_check(two_dir):
                continue
            one = chart[one_dir[0]][one_dir[1]]
            two = chart[two_dir[0]][two_dir[1]]
            if chart[i][j] == one == two:
                ans = chart[i][j]
                break

if ans == -1:
    print('ongoing')
else:
    print(ans)