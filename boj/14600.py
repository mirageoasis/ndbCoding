N=int(input())
row, col = map(int, input().split())

chart = [[0 for i in range(2 ** N)] for j in range(2 ** N)]

chart[len(chart) - col][row - 1] = -1
num=0


for i in chart:
    print(i)

def check(chart, x, y):
    pass

def cal(chart, x, y, l):
    global num
    new_l = l // 2
    num+=1

    cal(chart, , ,new_l)
    cal(chart, , ,new_l)
    cal(chart, , ,new_l)
    pass

cal(chart, 0, 0, len(chart))