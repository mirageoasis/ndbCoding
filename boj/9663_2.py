n=int(input())

ans=0

chart=[[0 for i in range(n)] for j in range(n)]
visit=[False for i in range(n)]

def check(row, col, num):
    global chart, n    
    # 대각선 check

    # _/
    for i in range(1,n):
        new_row=row+i
        new_col=col+i
        if 0<=new_row<n and 0<=new_col<n:
            chart[new_row][new_col]+=num
        else:
            break
    # \_
    for i in range(1,n):
        new_row=row+i
        new_col=col-i
        if 0<=new_row<n and 0<=new_col<n:
            chart[new_row][new_col]+=num
        else:
            break
    # /-
    for i in range(1,n):
        new_row=row-i
        new_col=col+i
        if 0<=new_row<n and 0<=new_col<n:
            chart[new_row][new_col]+=num
        else:
            break
    # -\
    for i in range(1,n):
        new_row=row-i
        new_col=col-i
        if 0<=new_row<n and 0<=new_col<n and chart[new_row][new_col]:
            chart[new_row][new_col]+=num
        else:
            break
    chart[row][col]+=num

def cal(idx):
    global ans, chart, n
    # row로 진행
    if idx == n:
        ans+=1
        return
    # col 이동
    for i in range(n):
        if not visit[i] and not chart[idx][i]:
            chart[idx][i]+=1
            visit[i]=True
            check(idx, i, 1)
            cal(idx+1)
            check(idx, i, -1)
            visit[i]=False
            chart[idx][i]-=1

cal(0)
print(ans)