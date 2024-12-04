from copy import deepcopy
# 27분 시작
row_len, col_len, cnt = map(int, input().split())

def cal_one():
    global row_len, col_len, chart
    new_chart=deepcopy(chart)
    
    for i in range(row_len):
        for j in range(col_len):
            chart[row_len-i-1][j]=new_chart[i][j]


def cal_two():
    global row_len, col_len, chart
    for idx, val in enumerate(chart):
        chart[idx]=val[::-1]


def cal_three():
    global row_len, col_len, chart
    new_chart=[[0 for i in range(row_len)] for j in range(col_len)]
    
    for i in range(row_len):
        for j in range(col_len):
            new_chart[j][row_len-i-1] = chart[i][j]

    chart=new_chart
    row_len=len(new_chart)
    col_len=len(new_chart[0])





def cal_four():
    global row_len, col_len, chart
    new_chart=[[0 for i in range(row_len)] for j in range(col_len)]
    
    for i in range(row_len):
        for j in range(col_len):
            new_chart[col_len-j-1][i] = chart[i][j]
    
    row_len=len(new_chart)
    col_len=len(new_chart[0])

    chart=new_chart
    row_len=len(new_chart)
    col_len=len(new_chart[0])

# 1 2 3 4 나누기
# 순서대로 


def div_four():
    global chart, row_len, col_len
    
    one=[[0 for i in range(col_len//2)] for j in range(row_len//2)] 
    two=[[0 for i in range(col_len//2)] for j in range(row_len//2)] 
    three=[[0 for i in range(col_len//2)] for j in range(row_len//2)] 
    four=[[0 for i in range(col_len//2)] for j in range(row_len//2)] 

    mid_row=row_len//2
    mid_col=col_len//2
    # 1번
    for i in range(mid_row):
        for j in range(mid_col):
            one[i][j]=chart[i][j]
    
    # 2번
    for i in range(mid_row):
        for j in range(mid_col):
            two[i][j]=chart[i][j+mid_col]
    
    # 3번
    for i in range(mid_row):
        for j in range(mid_col):
            three[i][j]=chart[i+mid_row][j+mid_col]
    
    # 4번
    for i in range(mid_row):
        for j in range(mid_col):
            four[i][j]=chart[i+mid_row][j]


    return one, two, three, four


def fill(one, two, three, four):
    global chart, row_len, col_len

    # one two three four에 넣는다.
    mid_row=row_len//2
    mid_col=col_len//2

    for i in range(mid_row):
        for j in range(mid_col):
            chart[i][j]=one[i][j]
    
    for i in range(mid_row):
        for j in range(mid_col):
            chart[i][j+mid_col]=two[i][j]

    for i in range(mid_row):
        for j in range(mid_col):
            chart[i+mid_row][j+mid_col]=three[i][j]
    
    for i in range(mid_row):
        for j in range(mid_col):
            chart[i+mid_row][j]=four[i][j]

def cal_five():
    global row_len, col_len, chart
    
    one, two, three, four = div_four()
    fill(four, one, two, three)

def cal_six():
    global row_len, col_len, chart
    
    one, two, three, four = div_four()
    fill(two, three, four, one)

chart=[]

for i in range(row_len):
    chart.append(list(map(int, input().split())))

def debug():
    for c in chart:
        for b in c:
            print(b, end=' ')
        print()

commands=list(map(int, input().split()))

#debug()

for command in commands:
    #print(command)

    if command == 1:
        cal_one()
    elif command == 2:
        cal_two()
    elif command == 3:
        cal_three()
    elif command == 4:
        cal_four()
    elif command == 5:
        cal_five()
    elif command == 6:
        cal_six()

debug()