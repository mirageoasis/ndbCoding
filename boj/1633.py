import sys

chart=[]
for line in sys.stdin:
    line = line.strip()
    if not line:  # 빈 줄이면 중단
        break
    a, b = map(int, line.split())
    chart.append((a,b))
    #print(a, b)

#print(chart)

dp=[[[0 for i in range(16)] for j in range(16)] for k in range(len(chart))]

def cal(index, w, b):
    global dp, chart
    if index == -1:
        return 0
    # 흰 선택
    if dp[index][w][b]:
        return dp[index][w][b]
    white=0
    black=0
    none=0
    if w > 0:
        white=cal(index-1, w-1, b)+chart[index][0]
    # 검 선택
    if b > 0:
        black=cal(index-1, w, b-1)+chart[index][1]

    # 안 선택
    none=cal(index-1, w, b)
    dp[index][w][b]=max(white, black, none)
    return dp[index][w][b]


print(cal(len(chart)-1, 15, 15))
