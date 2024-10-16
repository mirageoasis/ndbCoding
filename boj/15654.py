from itertools import permutations

N, K = map(int, input().split())
li= list(map(int, input().split()))
visit=[False for i in range(N)]

def permu(idx, t):
    global N, K
    if idx == K:
        ans.append(t.copy())
    for i in range(N):
        if not visit[i]:
            visit[i]=True
            t.append(li[i])
            permu(idx+1, t)
            t.pop()
            visit[i]=False


ans=[]
permu(0, [])
ans.sort()

for i in ans:
    kk=[str(k) for k in i]
    print(' '.join(kk))