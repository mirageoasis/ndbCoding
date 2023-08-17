from copy import deepcopy

N, M, R = map(int, input().split())

chart = []

for i in range(N):
    chart.append(list(map(int, input().split())))

cal_list = list(map(int, input().split()))

def cal_one(chart):
    c = deepcopy(chart)
    for i in range(N // 2):
        for j in range(M):
            temp = c[i][j]
            c[i][j] = c[N - i - 1][j]
            c[N - i - 1][j] = temp
    
    return c

def cal_two(chart):
    c = deepcopy(chart)
    for i in range(N):
        for j in range(M // 2):
            temp = c[i][j]
            c[i][j] = c[i][M - j - 1]
            c[i][M - j - 1] = temp
    
    return c

def cal_three(chart):
    (N, M) = (M, N)
    c = [[0 for i in range(N)] for j in range(M)]
    for i in range(N):
        for j in range(M):
            chart[]
    return c

def cal_four(chart):
    c = deepcopy(chart)
    
    pass

def cal_five():
    pass

def cal_six():
    pass

for cal in cal_list:
    #print(cal)

