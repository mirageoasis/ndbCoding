# 51분 시작
import sys
from bisect import bisect_left

N, M = map(int, input().split())

chart=[]
window=[]

for i in range(N):
    chart.append(list(sorted(map(int, sys.stdin.readline().split()))))
#print(chart)


for i in range(N):
    window.append((chart[i][0], i, 0))

window.sort()
idx=0
ans=(window[-1][0] - window[0][0])

def finder(window, num):
    left=0
    right=len(window)

    while left < right:
        mid=(left+right)//2

        if window[mid][0] < num:
            left=mid+1
        else:
            right=mid
    
    return left

while True:
    # 투포인터를 찾아서
    _, chart_idx, chart_idx_idx = window[idx]

    if chart_idx_idx == M-1:
        break

    window.insert(finder(window, chart[chart_idx][chart_idx_idx+1]), (chart[chart_idx][chart_idx_idx+1], chart_idx, chart_idx_idx+1))
    idx+=1
    #print(window, idx)
    #print(window[-1][0], window[idx][0])
    ans=min(window[-1][0] - window[idx][0], ans)

print(ans)
