import sys

'''
4 5
0 0 1 1 0
0 0 0 1 1
1 1 1 1 1
0 0 0 0 0
'''

def dfs(row, col, chart, n, m):

    if row < 0 or col < 0 or row > n - 1 or col > m - 1 or chart[row][col] != 0:
        return
    
    chart[row][col] = 2
    dfs(row - 1, col, chart, n, m)
    dfs(row + 1, col, chart, n, m)
    dfs(row, col - 1, chart, n, m)
    dfs(row, col + 1, chart, n, m)


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    chart = []

    for i in range(n):
        chart.append(list(map(int, input())))
    
    #print(chart)

    #input 다 받음
    ans = 0

    for i in range(n):
        for j in range(m):
            if chart[i][j] == 0:
                #print(i, j)
                dfs(i, j, chart, n, m)
                ans+=1
    print(ans)
        

main()