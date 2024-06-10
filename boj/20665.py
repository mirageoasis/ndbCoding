import sys

N, T, P = map(int, input().split())

sit=[-1 for i in range(N)]
chart = []
ans=12*60

def min_cal(start, end):
    hour = end // 100 - start // 100
    min = end % 100 - start % 100
    return hour * 60 + min

for i in range(T):
    start, end = map(int, sys.stdin.readline().split())
    chart.append((start, end))
    
chart.sort(key=lambda x: (x[0], min_cal(x[0], x[1])))

def dis_cal(idx):
    # 
    if sit[idx]!=-1:
        return -1
    left_idx=idx-1
    right_idx=idx+1
    while left_idx >=0 and sit[left_idx] == -1:
        left_idx-=1
    while right_idx < len(sit) and sit[right_idx] == -1:
        right_idx+=1

    if idx==0:
        return right_idx - idx
    if idx==len(sit) - 1:
        return idx - left_idx

    return min(idx - left_idx, right_idx - idx)

for people_idx, val in enumerate(chart):
    #100 * 100 * 500
    # print()
    # print(ans)
    start, end = val
    dis=[0 for i in range(N)]
    for i, v in enumerate(sit):
        s, e = chart[v]
        if start >= e:
            sit[i]=-1
    for i in range(N):
        dis[i] = dis_cal(i)
    maxi = max(dis)
    for i, v in enumerate(dis):
        if maxi == v:
            sit[i]=people_idx
            if i+1 == P:
                ans-=min_cal(start, end)
            break
    # print(start, end)
    # print(dis)
    # print(sit)
    # print(ans)


print(ans)