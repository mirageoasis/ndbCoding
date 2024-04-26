# 40000 까지의 소수를 구함

li = []


def p_list():
    lim = 40001
    number_chart = [True for i in range(lim)]
    # 마지막으로 탐색하고 list로 돌려줌
    number_chart[1] = False
    for i in range(2, lim):
        if number_chart[i]:
            for i in range(i*2, lim, i):
                number_chart[i] = False
    ret = []
    for i in range(1, lim):
        if number_chart[i]:
            ret.append(i)
    return ret

prime_list = p_list()
#print(len(prime_list))

N = int(input())

dp = [0 for i in range(N+1)]

dp = [0 for _ in range(N+1)]
dp[0] = 1

for p in prime_list:
    for i in range(p, N+1):
        dp[i] += dp[i - p]
        dp[i] %= 123456789

print(dp[N])