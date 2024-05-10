# 59분 시작
import sys

N=int(input())

chart = []

for i in range(N):
    chart.append(list(map(int, sys.stdin.readline().strip().split())))

row_chart = sorted([c[0] for c in chart])
col_chart = sorted([c[1] for c in chart])

# 백만 * 2는 ㄱㅊ다 아님?

# 맨 끝에서 
def cal(chart):
    start = sum([abs(chart[0] - c) for c in chart])
    ret = start
    #print(ret)
    # len - now_idx 만큼 minus고 
    # now_idx만큼 더한다.
    # 만약에 i가 now_idx와 같아진다면 now_idx를 늘려준다.
    
    now_idx=1

    for i in range(chart[0]+1, chart[-1]+1):
        start += - len(chart) + now_idx * 2
        if i == chart[now_idx]:
            while now_idx < len(chart) and chart[now_idx] <= i:
                now_idx+=1
        ret=min(ret, start)
        #print(i, ret, start)
    #print()
    return ret


#print(cal(row_chart) + cal(col_chart))

r_mid = row_chart[len(row_chart) // 2]
c_mid = col_chart[len(col_chart) // 2]
#print(r_mid)
#print(c_mid)

print(sum([abs(r_mid - r) for r in row_chart]) + sum([abs(c_mid - c) for c in col_chart]))