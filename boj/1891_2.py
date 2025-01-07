n, num = map(int, input().split())
col_mov, row_mov = map(int, input().split())
col_mov, row_mov  = col_mov, -row_mov

"""
21
34

0123
1123
2
3
"""
# 시작 점에서 길이가 length//2 부터 시작


def num_to_row_col(start_row, start_col, length, num, idx):
    if idx == len(num):
        return (start_row, start_col)
    half=length//2
    if num[idx] == '1':
        return num_to_row_col(start_row, start_col+half, half, num, idx+1)
    elif num[idx] == '2':
        return num_to_row_col(start_row, start_col, half, num, idx+1)
    elif num[idx] == '3':
        return num_to_row_col(start_row+half, start_col, half, num, idx+1)
    elif num[idx] == '4':
        return num_to_row_col(start_row+half, start_col+half, half, num, idx+1)

#print(num_to_row_col(0, 0, 2**n, str(num), 0))

target_row, target_col = num_to_row_col(0, 0, 2**n, str(num), 0)

target_row+=row_mov
target_col+=col_mov

def row_col_to_num(start_row, start_col, target_row, target_col, length, now_number):
    global n
    #print(now_number)
    #print(start_row, start_col, length, target_row, target_col)
    if len(now_number) == n:
        return now_number
    half=length//2
    row_half=start_row+length//2
    col_half=start_col+length//2
    if target_row >= row_half and target_col >= col_half:
        return row_col_to_num(start_row+half, start_col+half, target_row, target_col, half, now_number+"4")
    elif target_row >= row_half and target_col < col_half:
        return row_col_to_num(start_row+half, start_col, target_row, target_col, half, now_number+"3")
    elif target_row < row_half and target_col >= col_half:
        return row_col_to_num(start_row, start_col+half, target_row, target_col, half, now_number+"1")
    elif target_row < row_half and target_col < col_half:
        return row_col_to_num(start_row, start_col, target_row, target_col, half, now_number+"2")
if 0<=target_row<2**n and 0<=target_col<2**n:
    print(row_col_to_num(0, 0, target_row, target_col, 2**n, ""))
else:
    print(-1)