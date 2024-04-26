N = int(input())

chart = [[0 for i in range(N)] for j in range(N)]

# right down
# left down
# down

# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)
# (3,0) (3,1) (3,2) (3,3)

ans=0

def dfs(row):
    # idx 번 row에서 활동하는 것을 가정
    global ans
    if row == N:
        ans+=1
        return
    
    for col in range(N):
        if chart[row][col] == 0:
            chart[row][col] += 1
            #left down
            for i in range(row+1, N):
                if row+col-i >= 0:
                    chart[i][row+col-i] += 1
            #right down
            for i in range(row+1, N):
                if col+i-row < N:
                    chart[i][col+i-row] += 1
            #down
            for i in range(row+1, N):
                chart[i][col] += 1
            dfs(row+1)
            #left down
            for i in range(row+1, N):
                if row+col-i >= 0:
                    chart[i][row+col-i] -= 1
            #right down
            for i in range(row+1, N):
                if col+i-row < N:
                    chart[i][col+i-row] -= 1
            for i in range(row+1, N):
                chart[i][col] -= 1
            chart[row][col] -= 1



dfs(0)

print(ans)