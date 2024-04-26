N, M, K = map(int, input().split())

orders = []

for i in range(N):
    orders.append(list(map(int, input().split())))

idx_order_dict = {idx:val for idx, val in enumerate(orders)}
# 끝에서 부터 땡기는거 품목별로 하기

chart = [[0 for k in range(K + 1)] for j in range(M + 1)]
cnt=0
while cnt < N:
    now_order = idx_order_dict[cnt]
    for i in range(M, 0, -1):
        for j in range(K, 0, -1):
            # i는 치즈버거
            # j는 감튀
            if cnt == 0:
                if i >= now_order[0] and j >= now_order[1]:
                    chart[i][j] = chart[i - now_order[0]][j - now_order[1]] + 1
            else:
                if i >= now_order[0] and j >= now_order[1]:
                    chart[i][j] = max(chart[i][j], chart[i - now_order[0]][j - now_order[1]] + 1)
    # for c in chart:
    #     print(c)
    # print()
    
    cnt+=1

from itertools import chain

print(max(chain(*chart)))