s_row, s_col = map(int, input().split())
k_row, k_col = map(int, input().split())

INF=10000
visit = [[False for i in range(9)] for j in range(10)]
count = [[INF for i in range(9)] for j in range(10)]
ans=INF



def dfs(now_row, now_col, visit, count, depth):
    global k_row, k_col, ans
    #print((now_row, now_col), (k_row, k_col), depth)
    if count[now_row][now_col] < depth:
        return
    count[now_row][now_col] = depth
    if now_row == k_row and now_col == k_col:
        ans = min(ans, depth)
        return
    dr_o = [-1, -1, 1, 1, 0, 0, 0, 0]
    dc_o = [0, 0, 0, 0, 1, -1, -1, 1]

    dr_o_2 = [-2, -2, 2, 2, -1, -1, 1, 1]
    dc_o_2 = [1, -1, -1, 1, 2, -2, -2, 2]


    dr = [-3, -3, 3, 3, -2, -2, 2, 2]
    dc = [2, -2, -2, 2, 3, -3, -3, 3]
    
    for i in range(8):
        new_row = now_row + dr[i]
        new_col = now_col + dc[i]
        new_row_sub = now_row + dr_o[i]
        new_col_sub = now_col + dc_o[i]
        new_row_sub_2 = now_row + dr_o_2[i]
        new_col_sub_2 = now_col + dc_o_2[i]

        if not (new_row_sub == k_row and new_col_sub == k_col):
            if not (new_row_sub_2 == k_row and new_col_sub_2 == k_col):
                if 0 <= new_row < 10 and 0 <= new_col < 9 and not visit[new_row][new_col]:
                    dfs(new_row, new_col, visit, count, depth+1)

visit[s_row][s_col] = True
visit[s_row][s_col] = INF
dfs(s_row, s_col, visit, count, 0)
visit[s_row][s_col] = False

if ans != INF:
    print(ans)
else:
    print(-1)
