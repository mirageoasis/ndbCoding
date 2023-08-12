import bisect

N, H = map(int, input().split())

total_list = []

for i in range(N):
    total_list.append(int(input()))

def v1(total_list):
    up_list = [i for idx, i in enumerate(total_list) if idx % 2 != 0]
    down_list = [i for idx, i in enumerate(total_list) if idx % 2 == 0]

    up_sum = [0 for i in range(H)]
    down_sum = [0 for i in range(H)]

    for i in up_list:
        up_sum[H - i] += 1

    for i in down_list:
        down_sum[i - 1] += 1

    for i in range(1, H):
        up_sum[i] += up_sum[i-1]

    for i in range(H - 2, -1, -1):
        down_sum[i] += down_sum[i+1]


    total_sum = [i+j for i, j in zip(up_sum, down_sum)]

    #print(total_sum)

    mini = min(total_sum)

    cnt = total_sum.count(mini)

    print(mini, cnt)


#v2

def v2(total_list):
    up_list = [i for idx, i in enumerate(total_list) if idx % 2 != 0]
    down_list = [i for idx, i in enumerate(total_list) if idx % 2 == 0]

    up_list.sort()
    down_list.sort()

    total_cnt = [0 for i in range(H)]

    for i in range(H):
        #up 에서 찾기
        #down 에서 찾기
        up_pos = H - i
        down_pos = i + 1

        up_cnt = len(up_list) - bisect.bisect_left(up_list, up_pos)
        down_cnt = len(down_list) - bisect.bisect_left(down_list, down_pos)
        total_cnt[i] = up_cnt + down_cnt

    mini = min(total_cnt)
    cnt = total_cnt.count(mini)
    print(mini, cnt)

v2(total_list)