n=int(input())
t_col, t_row = map(int, input().split())

chart = [
    [0 for i in range(2**n)] for i in range(2**n)
]

t_row=2**n-t_row
t_col=t_col-1

total_number=1

def find_out(start_row, start_col, end_row, end_col, target_row, target_col):
    global total_number, t_row, t_col
    # 앞의 절반은 start_row, row_middle까지
    # 뒤의 절반은 row_middle+1, end_row
    if start_row == end_row:
        return

    row_middle=(start_row+end_row)//2
    col_middle=(start_col+end_col)//2

    # 1 2
    # 3 4
    target1_row, target1_col = row_middle, col_middle
    target2_row, target2_col = row_middle, col_middle+1
    target3_row, target3_col = row_middle+1, col_middle
    target4_row, target4_col = row_middle+1, col_middle+1

    if target_row <=row_middle and target_col <=col_middle:
        # 1섹터
        chart[target2_row][target2_col]=total_number
        chart[target3_row][target3_col]=total_number
        chart[target4_row][target4_col]=total_number
        target1_row, target1_col = target_row, target_col
    elif target_row <=row_middle and target_col > col_middle:
        # 2섹터
        chart[target1_row][target1_col]=total_number
        chart[target3_row][target3_col]=total_number
        chart[target4_row][target4_col]=total_number
        target2_row, target2_col = target_row, target_col
    elif target_row > row_middle and target_col <= col_middle:
        # 3섹터
        chart[target2_row][target2_col]=total_number
        chart[target1_row][target1_col]=total_number
        chart[target4_row][target4_col]=total_number
        target3_row, target3_col = target_row, target_col
    elif target_row > row_middle and target_col > col_middle:
        # 4섹터
        chart[target2_row][target2_col]=total_number
        chart[target3_row][target3_col]=total_number
        chart[target1_row][target1_col]=total_number
        target4_row, target4_col = target_row, target_col
    
    total_number+=1
    # 1 섹터
    find_out(start_row, start_col, row_middle, col_middle, target1_row, target1_col)
    # 2 섹터
    find_out(start_row, col_middle+1, row_middle, end_col, target2_row, target2_col)
    # 3 섹터
    find_out(row_middle+1, start_col, end_row, col_middle, target3_row, target3_col)
    # 4 섹터
    find_out(row_middle+1, col_middle+1, end_row, end_col, target4_row, target4_col)
chart[t_row][t_col]=-1

find_out(0, 0, 2**n-1, 2**n-1, t_row, t_col)

for c in chart:
    print(' '.join([str(i) for i in c]))