from itertools import permutations

n, m, h = map(int, input().split())
chart = [list(map(int, input().split())) for _ in range(n)]

start_row = start_col = 0
pt_list = []

for i in range(n):
    for j in range(n):
        if chart[i][j] == 1:
            start_row, start_col = i, j
        elif chart[i][j] == 2:
            pt_list.append((i, j))

ans = 0

for order in permutations(pt_list):
    now_health = m
    now_row, now_col = start_row, start_col
    visited_cnt = 0

    for to_row, to_col in order:
        dist = abs(to_row - now_row) + abs(to_col - now_col)
        if now_health < dist:  # 다음 점까지 못 가면 종료
            break

        now_health -= dist
        now_health += h
        visited_cnt += 1
        now_row, now_col = to_row, to_col

        back_dist = abs(start_row - now_row) + abs(start_col - now_col)
        if now_health >= back_dist:
            ans = max(ans, visited_cnt)

print(ans)
