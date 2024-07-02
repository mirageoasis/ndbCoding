# 43분
import sys

row_len, col_len = map(int, input().split())
T=int(input())

chart=[]
test_case=[]
j_chart=[[0 for i in range(col_len)] for j in range(row_len)]
i_chart=[[0 for i in range(col_len)] for j in range(row_len)]
o_chart=[[0 for i in range(col_len)] for j in range(row_len)]

for i in range(row_len):
    chart.append(list(sys.stdin.readline()))

for i in range(T):
    a, b, c, d = map(int, sys.stdin.readline().split())
    # 1씩빼서 맞춰야함.
    test_case.append(((a-1, b-1), (c-1, d-1)))


def make_chart(target_chart, target_case):
    #'J''I''O'
    for i in range(row_len):
        for j in range(col_len):
            if chart[i][j] == target_case:
                target_chart[i][j]=1

def plus_chart(target_chart):
    # col 방향으로 더하기
    for i in range(row_len):
        for j in range(1, col_len):
            target_chart[i][j] += target_chart[i][j-1]
    
    for i in range(col_len):
        for j in range(1, row_len):
            target_chart[j][i] += target_chart[j-1][i]

make_chart(j_chart, 'J')
make_chart(i_chart, 'I')
make_chart(o_chart, 'O')

plus_chart(j_chart)
plus_chart(i_chart)
plus_chart(o_chart)

# for i in j_chart:
#     print(i)

# print()

# for i in o_chart:
#     print(i)

# print()

# for i in i_chart:
#     print(i)

# print()

def chart_cal(target_chart, first, second):
    first_row, first_col = first
    second_row, second_col = second

    p = target_chart[first_row-1][first_col-1] if (first_row!=0 and first_col!=0) else 0
    m_1 = target_chart[first_row-1][second_col] if (first_row!=0) else 0
    m_2 = target_chart[second_row][first_col-1] if (first_col!=0) else 0
    #print(target_chart[second_row][second_col], m_1, m_2, p)

    return target_chart[second_row][second_col] - m_1 - m_2 + p


for first, second in test_case:
    

    j_count = chart_cal(j_chart, first, second)
    o_count = chart_cal(o_chart, first, second)
    i_count = chart_cal(i_chart, first, second)
    print(j_count, o_count, i_count)
    #print()

