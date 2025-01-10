import sys
row_len, col_len = map(int, input().split())
test_case=int(input())
chart=[]

for i in range(row_len):
    chart.append(list(sys.stdin.readline().strip()))

i_chart=[[0 for j in range(col_len+1)] for i in range(row_len+1)]
j_chart=[[0 for j in range(col_len+1)] for i in range(row_len+1)]
o_chart=[[0 for j in range(col_len+1)] for i in range(row_len+1)]

for i in range(row_len):
    for j in range(col_len):
        if chart[i][j] == 'I':
            i_chart[i+1][j+1]+=1
        elif chart[i][j] == 'J':
            j_chart[i+1][j+1]+=1
        elif chart[i][j] == 'O':
            o_chart[i+1][j+1]+=1

for i in range(1, row_len+1):
    for j in range(1, col_len+1):
        i_chart[i][j]+=i_chart[i][j-1]
        j_chart[i][j]+=j_chart[i][j-1]
        o_chart[i][j]+=o_chart[i][j-1]

for i in range(1, row_len+1):
    for j in range(1, col_len+1):
        i_chart[i][j]+=i_chart[i-1][j]
        j_chart[i][j]+=j_chart[i-1][j]
        o_chart[i][j]+=o_chart[i-1][j]


def ans_chart(chart, s_row, s_col, e_row, e_col):
    total = chart[e_row][e_col]
    c_min = chart[e_row][s_col-1]
    r_min = chart[s_row-1][e_col]
    return total - c_min - r_min + chart[s_row-1][s_col-1]


for _ in range(test_case):
    s_row, s_col, e_row, e_col = map(int, sys.stdin.readline().split())
    
    i = ans_chart(i_chart, s_row, s_col, e_row, e_col)
    j = ans_chart(j_chart, s_row, s_col, e_row, e_col)
    o = ans_chart(o_chart, s_row, s_col, e_row, e_col)

    print(j, o, i)

