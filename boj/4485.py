import sys
from collections import defaultdict, deque
import heapq

INF=9999999
chart=[]
dist_chart=[]
way=defaultdict(list)
visit=[]
N=0

def moveable(row, col):
    if 0<=row< N and 0<=col< N:
        return True
    return False


def bfs():
    heap=[]
    heap.append((0, 0, 0))

    while heap:
        #print(heap)
        dist, row, col= heapq.heappop(heap)
        #print(dist, row, col)
        if row == N-1 and col == N-1:
            return dist+chart[0][0]
        
        if dist > dist_chart[row][col]:
            continue
        
        for new_row, new_col in way[(row, col)]:
            if dist_chart[new_row][new_col] > chart[new_row][new_col] + dist:
                dist_chart[new_row][new_col]=chart[new_row][new_col] + dist
                heapq.heappush(heap, (dist_chart[new_row][new_col], new_row, new_col))




cnt=1
while True:
    N=int(input())
    chart=[]
    way=defaultdict(list)
    dist_chart=[[INF for i in range(N)] for j in range(N)]
    visit=[[False for i in range(N)]for j in range(N)]

    if N == 0:
        break

    for i in range(N):
        chart.append(list(map(int, sys.stdin.readline().split())))
    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if moveable(i+dx[k], j+dy[k]):
                    way[(i, j)].append((i+dx[k], j+dy[k]))
    
    dist_chart[0][0]=0
    visit[0][0]=True
    print(f"Problem {cnt}: {bfs()}")
    cnt+=1
