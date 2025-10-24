INF=1000000000


def all_cal():
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.' and not visit[i][j]:
                return False
    return True

def cal(row, col, count):
    global ans
    dr=[1, -1, 0, 0]
    dc=[0, 0, 1, -1]
    if all_cal():
        ans=min(count-1, ans)
        return
    if count >= ans:
        return
    
    for i in range(4):
        r,c = row, col
        stack=[]
        while True:
            r+=dr[i]
            c+=dc[i]
            #print(row, col, n, m, visit[row][col], board[row][col])
            if 0<=r<n and 0<=c<m and not visit[r][c] and board[r][c] == '.':
                visit[r][c]=True
                stack.append((r, c))
            else:
                break
            
        if stack:
            new_row, new_col = stack[-1]
            cal(new_row, new_col, count + 1)

        for s in stack:
            visit[s[0]][s[1]] = False


case=0
while True:
    try:
        n, m = map(int, input().split())
        board = [list(input().strip()) for _ in range(n)]
        ans=INF
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    visit = [[False for j in range(m)] for _ in range(n)]
                    visit[i][j]=True
                    cal(i, j, 1)
                    #visit[i][j]=False
        case += 1
        print(f"Case {case}: {ans if ans != INF else -1}")
    except Exception as e:
        print(e)
        break