# 37분 시작
from itertools import combinations

# combination이므로 visited 를 하고 현재 idx보다 큰거
N, M = map(int, input().split())

visit=[False for i in range(N)]

def combi(li, idx, step):
    global N, M
    if M == step:
        #print(M, step)
        #print(visit)
        for i in range(0, N):
            if visit[i]:
                print(li[i], end=' ')
        print()
        return

    for i in range(idx+1, N):
        visit[i]=True
        combi(li, i, step+1)
        visit[i]=False


li=list(sorted(map(int, input().split())))


combi(li, -1, 0)