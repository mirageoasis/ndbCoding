from collections import deque

n, m = map(int, input().split())
chart = []
for i in range(n):
    chart.append(list(map(int, input())))

# 1이면 safe 0 이면 not safe

d_r = [1, -1, 0, 0]
d_c = [0, 0, 1, -1]

def bfs():

    q = deque()
    q.append((0,0,1))
    chart[0][0] = 2

    while q:
        row, col, cnt = q.popleft()
        #print(row, col, cnt)
        if n - 1 == row and m - 1 == col:
            print(cnt)
            return cnt
        
        for i in range(4):
            n_r = row + d_r[i]
            n_c = col + d_c[i]
            if -1 < n_r < n and -1 < n_c < m and chart[n_r][n_c] == 1:
                q.append((n_r, n_c, cnt+1))
                chart[n_r][n_c] = 2



def main():

    bfs()
    



main()