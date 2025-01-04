from collections import deque
n=int(input())

INF=99999999
chart=[]
visit=[[False for i in range(n)]for j in range(n)]
length_chart=[[0 for i in range(n)]for j in range(n)]

for i in range(n):
    chart.append(list(map(int, input().split())))

def bfs(start_row, start_col, cnt):
    global n, chart, visit
    que=deque()
    que.append((start_row, start_col))
    d_r=[1, -1, 0, 0]
    d_c=[0, 0, -1, 1]
    while que:
        now_row, now_col = que.popleft()
        chart[now_row][now_col]=cnt
        for i in range(4):
            new_row = now_row + d_r[i]
            new_col = now_col + d_c[i]
            if 0<=new_row<n and 0<=new_col<n and not visit[new_row][new_col] and chart[new_row][new_col] == 1:
                visit[new_row][new_col]=True
                que.append((new_row, new_col))

cnt=2
for row in range(n):
    for col in range(n):
        if chart[row][col] == 1 and not visit[row][col]:
            visit[row][col]=True
            bfs(row, col, cnt)
            cnt+=1

# for c in chart:
#     print(c)
# 다시한번 초기화
visit=[[False for i in range(n)]for j in range(n)]
# 섬 생성 완료
# 바닷가 땅 배열에 넣기
# 주변 바닷가인지
# 주변 섬인지 알아보기, (자신은 제외)

def around_sea(row, col):
    global n, chart, visit
    d_r=[1,-1,0,0]
    d_c=[0,0,-1,1]
    for i in range(4):
        new_row = row + d_r[i]
        new_col = col + d_c[i]
        if 0<=new_row<n and 0<=new_col<n and chart[new_row][new_col] == 0 and chart[row][col] != 0:
            return True
    return False

def around_land(row, col, origin):
    global n, chart, visit, length_chart
    d_r=[1,-1,0,0]
    d_c=[0,0,-1,1]
    mini=INF
    for i in range(4):
        new_row = row + d_r[i]
        new_col = col + d_c[i]
        if 0<=new_row<n and 0<=new_col<n and chart[new_row][new_col] != 0 and chart[new_row][new_col] != origin:
            mini=min(mini, length_chart[new_row][new_col])
    return mini

que=deque()

for row in range(n):
    for col in range(n):
        if around_sea(row, col):
            visit[row][col]=True
            que.append((row, col, chart[row][col], 0))

for c in chart:
    print(c)

#print(shore_land)
# 해안선 확보
ans=INF
while que:
    now_row, now_col, now_land_number, now_length = que.popleft()
    # 만약에 방문하지 않았고, 바다라서 자신으로 매립한다. 그리고 length에는 현재 거리를 기록
    if around_land(now_row, now_col, chart[now_row][now_col]) != INF:
        ans= min(ans,now_length+around_land(now_row, now_col, chart[now_row][now_col]))
        continue
    d_r=[1,-1,0,0]
    d_c=[0,0,-1,1]
    for i in range(4):
        new_row=now_row+d_r[i]
        new_col=now_col+d_c[i]
        if 0<=new_row<n and 0<=new_col<n and not visit[new_row][new_col]:
            visit[new_row][new_col]=True
            length_chart[new_row][new_col]=now_length+1
            chart[new_row][new_col]=now_land_number
            que.append((new_row, new_col,now_land_number, now_length+1))
    print()
    for c in chart:
        print(c)
print(ans)
for c in chart:
    print(c)