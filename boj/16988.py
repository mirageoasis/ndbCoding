from itertools import combinations
from collections import deque

N, M = map(int, input().split(' '))

chart = []
ans = 0

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def score(N, M, original_row, original_col, chart, visited):
    # bfs로 순회하면서 옆에 0이 있는지 확인
    temp_ans = 0
    q = deque()
    q.append((original_row, original_col))
    flag = True
    # 개수 세기
    while q:
        row, col = q.pop()
        temp_ans +=1
        
        for i in range(4):
            new_row = row + dr[i]
            new_col = col + dc[i]

            if -1 < new_row < N and -1 < new_col < M:
                if chart[new_row][new_col] == 0:
                    flag = False
                
                if not visited[new_row][new_col] and chart[new_row][new_col] == 2:
                    visited[new_row][new_col] = True
                    q.append((new_row, new_col))

    if flag:
        return temp_ans
    else:
        return 0
    


def cal(N, M, chart):
    global ans
    temp_ans = 0
    visited = [[False for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            if chart[i][j] == 2 and not visited[i][j]:
                visited[i][j] = True
                temp_ans += score(N, M, i, j, chart, visited)
    ans = max(ans, temp_ans)


for i in range(N):
    chart.append(list(map(int, input().split(' '))))

# 경우의 수 400 C 2 -> 가능
# 한번의 오목 수당 얼마나 죽을 수 있을까를 계산하는 것이 관건
# 20 * 20 
# 모든 칸을 점검할 때 0이 없다면 죽었다고 가정한다.
# 0을 가지는 리스트

zero_list = [(i, j) for i in range(N) for j in range(M) if chart[i][j] == 0]
iter_range = combinations(zero_list, 2)


for one, two in list(iter_range):
    chart[one[0]][one[1]] = 1
    chart[two[0]][two[1]] = 1
    cal(N, M, chart)
    chart[one[0]][one[1]] = 0
    chart[two[0]][two[1]] = 0



print(ans)