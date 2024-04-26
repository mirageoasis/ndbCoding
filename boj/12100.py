import copy

# 위
# 아래
# 왼
# 오
# 각각 라인을 쭉 미는 방식으로
ans = 0

def pull_all(li: list):
    ret = li.copy()
    
    last_idx = 0 # 겹쳐볼 index
    
    for idx, val in enumerate(ret):
        if val == 0:
            continue
        if idx == 0:
            continue
        #print(ret)
        ret[idx] = 0
        if ret[last_idx] == 0:
            ret[last_idx] = val
        elif ret[last_idx] == val:
            ret[last_idx] = val * 2
            last_idx+=1
        else:
            ret[last_idx+1] = val
            last_idx+=1

    return ret

N = int(input())
chart = []

for i in range(N):
    chart.append(list(map(int, input().split())))


def left(chart, N):
    cal_chart = copy.deepcopy(chart)

    for i in range(N):
        cal_chart[i] = pull_all(cal_chart[i])

    return cal_chart

def right(chart, N):
    cal_chart = copy.deepcopy(chart)

    for i in range(N):
        cal_chart[i] = pull_all(cal_chart[i][::-1])[::-1]

    return cal_chart

def up(chart, N):
    cal_chart = copy.deepcopy(chart)

    for i in range(N):
        t = []
        for x in range(N):
            for y in range(N):
                if y == i:
                    t.append(chart[x][y])

        cal_temp = pull_all(t)

        for x in range(N):
            for y in range(N):
                if y == i:
                    cal_chart[x][y] = cal_temp[x]

    return cal_chart

def down(chart, N):
    cal_chart = copy.deepcopy(chart)

    for i in range(N):
        t = []
        for x in range(N):
            for y in range(N):
                if y == i:
                    t.append(chart[x][y])

        cal_temp = pull_all(t[::-1])

        for x in range(N):
            for y in range(N):
                if y == i:
                    cal_chart[N-x-1][y] = cal_temp[x]

    return cal_chart

def dfs(chart, times, lim, N):
    global ans
    if times > lim:
        for i in range(N):
            for j in range(N):
                ans = max(ans, chart[i][j])
        return
    
    # 왼
    cal_chart = left(chart, N)
    dfs(cal_chart, times+1, lim, N)

    # 오른쪽
    cal_chart = right(chart, N)
    dfs(cal_chart, times+1, lim, N)

    # 위쪽
    cal_chart = up(chart, N)
    dfs(cal_chart, times+1, lim, N)

    # 아래쪽
    cal_chart = down(chart, N)
    dfs(cal_chart, times+1, lim, N)

dfs(chart, 1, 5, N)
print(ans)

"""
4
2 4 2 2
4 4 2 2 
2 0 0 2
0 2 2 0
"""