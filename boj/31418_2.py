import sys

col_len, row_len, k, t = map(int, input().split())

virus=[]

ans=1
for i in range(k):
    col, row = map(int, sys.stdin.readline().split())
    row-=1
    col-=1
    
    high=max(0, row-t)
    low=min(row_len-1, row+t)
    left=max(0, col-t)
    right=min(col_len-1, col+t)    

    row_cal=low-high+1
    col_cal=right-left+1
    
    ans = (ans * row_cal * col_cal) % 998244353


print(ans)