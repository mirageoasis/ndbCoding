piece, num = map(int, input().split())
col, row = map(int, input().split())
num=str(num)

start_row=0
end_row=2**piece

start_col=0
end_col=2**piece

def cal(start_row, end_row, start_col, end_col, depth):
    # 현재 row와 현재 col에서 상대적인 위치로 계산한다.
    mid_row = (start_row + end_row) // 2
    mid_col = (start_col + end_col) // 2
    #print(start_row, end_row, start_col, end_col)
    if depth == len(num):
        return (mid_row, mid_col)
    
    if num[depth] == '1':
        return cal(start_row, mid_row, mid_col, end_col, depth+1)
    elif num[depth] == '2':
        return cal(start_row, mid_row, start_col, mid_col, depth+1)
    elif num[depth] == '3':
        return cal(mid_row, end_row, start_col, mid_col, depth+1)
    elif num[depth] == '4':
        return cal(mid_row, end_row, mid_col, end_col, depth+1)

def convert(start_row, end_row, start_col, end_col, depth, ans):
    if depth == len(num):
        return ans
    #print(ans)
    #print(start_row, end_row, start_col, end_col, new_row, new_col)
    mid_row = (start_row + end_row) // 2
    mid_col = (start_col + end_col) // 2

    if start_row <= new_row < mid_row and mid_col <= new_col < end_col:
        return convert(start_row, mid_row, mid_col, end_col, depth+1, ans + '1')
    elif start_row <= new_row < mid_row and start_col <= new_col < mid_col:
        return convert(start_row, mid_row, start_col, mid_col, depth+1, ans + '2')
    elif mid_row <= new_row < end_row and start_col <= new_col < mid_col:
        return convert(mid_row, end_row, start_col, mid_col, depth+1, ans + '3')
    elif mid_row <= new_row < end_row and  mid_col <= new_col < end_col :
        return convert(mid_row, end_row, mid_col, end_col, depth+1, ans + '4')

now_row, now_col = cal(start_row, end_row, start_col, end_col, 0)
new_row, new_col = (now_row-row, now_col+col)

#print(now_row, now_col)
a = convert(0, 2**piece, 0, 2**piece, 0, '')
print(a if a else -1)