from collections import deque
from sys import stdin


T=int(input())


for _ in range(T):
    que=deque()
    # N은 건물 개수, K는 의존개수
    N, K = map(int, input().split())
    #  건물 당 소요시간
    time_chart=list(map(int, input().split()))
    # 1 맞춰주기
    time_chart.insert(0, 0)
    dependency_chart=[[] for i in range(N+1)]
    dependency_count=[0 for i in range(N+1)]
    ans_chart=[0 for i in range(N+1)]

    for i in range(K):
        a, b = map(int, stdin.readline().split())
        dependency_chart[a].append(b)
        dependency_count[b]+=1
    #목표 건물
    W=int(input())
    
    for i in range(1, N+1):
        if dependency_count[i] == 0:
            que.append(i)

    while que:
        node = que.popleft()

        for i in dependency_chart[node]:
            dependency_count[i]-=1
            ans_chart[i]=max(ans_chart[i], ans_chart[node]+time_chart[node])
            if dependency_count[i] == 0:
                que.append(i)
    
    print(ans_chart[W]+time_chart[W])


