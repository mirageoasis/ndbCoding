# 8방향
# 숫자는 n * row + col
import sys
chart=[]
row_len, col_len = map(int, input().split())

for _ in range(row_len):
    chart.append(list(map(int, sys.stdin.readline().split())))

# 전부 다하면 시간초과 날 것 같음-> 메모이제이션

def rowcol_tonum(row, col):
    global col_len
    return col_len * row + col

def num_to_row(num):
    global col_len
    return num // col_len

def num_to_col(num):
    global row_len
    return num % col_len

parent=[i for i in range(row_len*col_len)]

def parent_find(number):
    global parent
    if parent[number] != number:
        parent[number] = parent_find(parent[number])
    return parent[number]

# 앞이 메인, 뒤에가 sub
def union(first, second):
    global parent
    first=parent_find(first)
    second=parent_find(second)
    parent[second]=first


for row in range(row_len):
    for col in range(col_len):
        d_r=[1,-1, 0, 0, 1, -1,1, -1]
        d_c=[0, 0, 1, -1,1, -1,-1, 1]
        # 자신을 부모라고 생각한다.
        parent_num=rowcol_tonum(row, col)
        origin_num=rowcol_tonum(row, col)
        mini=chart[row][col]
        for i in range(8):
            new_row=row+d_r[i]
            new_col=col+d_c[i]
            if 0<=new_row<row_len and 0<=new_col<col_len:
                if chart[new_row][new_col] < mini:
                    mini=chart[new_row][new_col]
                    parent_num=rowcol_tonum(new_row, new_col)
        
        if parent_num != origin_num:
            union(parent_num, origin_num)

for row in range(row_len):
    for col in range(col_len):
        now_num=rowcol_tonum(row, col)
        parent_find(now_num)

ans=[[0 for i in range(col_len)] for j in range(row_len)]
for row in range(row_len):
    for col in range(col_len):
        old_parent=rowcol_tonum(row, col)
        update_parent=parent_find(old_parent)
        new_row=num_to_row(update_parent)
        new_col=num_to_col(update_parent)
        ans[new_row][new_col]+=1

for a in ans:
    print(*a)
# 자바 연습하는 겸 한건데, 빠르게 풀꺼면 그냥 parent배열을 tuple로 만들어도 무상관.