row_len, col_len = map(int, input().split())

chart=[[True for i in range(col_len)] for j in range(row_len)]

queen_list=[]
knight_list=[]
pawn_list=[]

def init():
    li=list(map(int, input().split()))[1:]
    ret=[]
    for i in range(0, len(li), 2):
        ret.append((li[i]-1, li[i+1]-1))
    return ret

queen_list=init()
knight_list=init()
pawn_list=init()

all_set=set(queen_list + knight_list + pawn_list)

for r, c in pawn_list:
    chart[r][c]=False

for r, c in knight_list:
    d_r=[1,-1,1,-1,2,-2,2,-2]
    d_c=[2,2,-2,-2,1,1,-1,-1]
    chart[r][c]=False

    for i in range(8):
        new_row=r+d_r[i]
        new_col=c+d_c[i]
        if 0<=new_row<row_len and 0<=new_col<col_len:
            chart[new_row][new_col]=False

for r, c in queen_list:
    chart[r][c]=False
    # 위
    for i in range(r-1, -1, -1):
        new_row=i
        if (new_row, c) in all_set:
            break
        chart[new_row][c]=False
    
    # 아래
    for i in range(r+1, row_len):
        new_row=i
        if (new_row, c) in all_set:
            break
        chart[new_row][c]=False
    
    # 왼쪽
    for i in range(c-1, -1, -1):
        new_col=i
        if (r, new_col) in all_set:
            break
        chart[r][new_col]=False

    # 오른쪽
    for i in range(c+1, col_len):
        new_col=i
        if (r, new_col) in all_set:
            break
        chart[r][new_col]=False
    maxi=max(row_len, col_len)
    # 왼위
    for i in range(1, maxi):
        new_row=r-i
        new_col=c-i
        if 0<=new_row<row_len and 0<=new_col<col_len and not ((new_row,new_col) in all_set):
            chart[new_row][new_col]=False
        else:
            break
    # 우아
    for i in range(1, maxi):
        new_row=r+i
        new_col=c+i
        if 0<=new_row<row_len and 0<=new_col<col_len and not ((new_row,new_col) in all_set):
            chart[new_row][new_col]=False
        else:
            break
    # 왼아
    for i in range(1, maxi):
        new_row=r+i
        new_col=c-i
        if 0<=new_row<row_len and 0<=new_col<col_len and not ((new_row, new_col) in all_set):
            chart[new_row][new_col]=False
        else:
            break
    # 오위
    for i in range(1, maxi):
        new_row=r-i
        new_col=c+i
        if 0<=new_row<row_len and 0<=new_col<col_len and not ((new_row,new_col) in all_set):
            chart[new_row][new_col]=False
        else:
            break

print(sum([c.count(True) for c in chart]))