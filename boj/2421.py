N=int(input())
lim=1000000
chart = [1 for i in range(lim)]

chart[0] = 0
chart[1] = 0
for i in range(2, lim):
    if chart[i] == 1:
        for j in range(i*2, lim, i):
            chart[j] = 0

# 완탐은 아닌데.
ans = [[0 for i in range(1000)] for j in range(1000)]

# row가 앞에 col이 뒤에
ans[1][1] = 0

def few_ten(n):
    ret = 10
    while n >= ret:
        ret*=10
    return ret

for i in range(2, 1000):
    num = int(str(1) + str(i))
    ans[1][i] = ans[1][i-1] + chart[num]
    

for i in range(2, 1000):
    num = int(str(i) + str(1))
    ans[i][1] = ans[i-1][1] + chart[num]

for i in range(2, 1000):
    for j in range(2, 1000):
        num = int(str(i) + str(j))
        ans[i][j] = max(ans[i][j - 1], ans[i - 1][j]) + chart[num]

# for i in ans[:5]:
#     print(i[:5])

print(ans[N][N])
