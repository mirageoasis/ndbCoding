def solution():
    R, C = map(int, input().split())
    t = list(map(int, input().split()))
    #print(t)
    li = []
    chart = [[-1 for _ in range(R)] for __ in range(C)]
    for i in range(R):
        ti = []
        for j in range(C):
            ti.append(t[i * C + j])
        li.append(ti)

    for i in range(1 ,C):
        for j in range(R):
            if j == 0:
                li[j][i] += max(li[j][i-1],li[j+1][i-1])
            elif j == R - 1:
                li[j][i] += max(li[j][i-1],li[j-1][i-1])
            else:
                li[j][i] += max(li[j+1][i-1],li[j][i-1],li[j-1][i-1])
    ans = []
    for i in range(R):
        ans.append(li[i][C-1])
    print(max(ans))
"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""

N = int(input())

for i in range(N):
    solution()
