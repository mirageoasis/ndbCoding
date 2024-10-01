from bisect import bisect_left, bisect_right

N=int(input())
chart=list(map(int, input().split()))

chart.sort()
visit=[0 for i in range(len(chart)+1)]
ans=0
# i 는 시작 j는 끝
for i in range(len(chart)):
    for j in range(i+1, len(chart)):
        k=chart[i]+chart[j]
        #print(chart[i], chart[j], bisect_right(chart, k)-bisect_left(chart, k))
        left=bisect_left(chart, k)
        right=bisect_right(chart, k)
        if right - left > 0:
            # right left 섞으면 ㄱㄴ
            if chart[i] == 0:
                pass
            elif chart[j] == 0:
                pass
            elif chart[i] == 0 and chart[j] == 0:
                pass
            
            visit[left]+=1
            visit[right]-=1

        
        #ans+=bisect_right(chart, k)-bisect_left(chart, k)

print(visit.count(True))
