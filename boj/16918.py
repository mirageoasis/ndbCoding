# 05분 
# 40000 * 200

import sys

row_len, col_len, second = map(int, input().split())

chart = []

# -1 을 아무것도 없는 곳으로 설정
# 0은 폭탄이 설치되었음

for i in range(row_len):
    chart.append(list(sys.stdin.readline().strip()))

def dump_chart():
    for i in chart:
        print(i)

    print()

#dump_chart()

for i in range(row_len):
    for j in range(col_len):
        if chart[i][j] == '.':
            chart[i][j]=-1
        elif chart[i][j] == 'O':
            chart[i][j]=0

#dump_chart()
for i in range(0, second):
    if i == 0:
        for i in range(row_len):
            for j in range(col_len):
                if chart[i][j] == 0:
                    chart[i][j]+=1
    else:
        # 1차로 숫자를 늘린다.
        # 2차로 3이 도달한 숫자가 있다면 폭*파
        for i in range(row_len):
            for j in range(col_len):
                chart[i][j]+=1
        point=[]
        for row in range(row_len):
            for col in range(col_len):
                if chart[row][col] == 3:
                    dx=[0, 0, 1, -1]
                    dy=[1, -1, 0, 0]
                    chart[row][col]=-1
                    for i in range(4):
                        new_row=row+dx[i]
                        new_col=col+dy[i]
                        if 0<=new_row<row_len and 0<=new_col<col_len:
                            point.append((new_row, new_col))

        for n_r, n_c in point:
            chart[n_r][n_c]=-1



    #dump_chart()


for i in range(row_len):
    for j in range(col_len):
        if chart[i][j] != -1:
            print('O' ,end='')
        else:
            print('.' ,end='')
    print()

'''
0
000
0b0
000

1
000
010
000

2
bbb
b2b
bbb

3
101
000
101

4
2b2
bbb
2b2

5
313    000
111 -> 010
313    000


'''