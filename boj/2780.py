import sys
T=int(input())

cord = set()
cord.add((0, 0))
cord.add((0, 1))
cord.add((0, 2))

cord.add((1, 0))
cord.add((1, 1))
cord.add((1, 2))

cord.add((2, 0))
cord.add((2, 1))
cord.add((2, 2))

cord.add((3, 0))

MOD=1234567

def movable(row, col):
    global cord
    return (row, col) in cord

chart=[[[0,0,0],[0,0,0],[0,0,0],[0]] for i in range(1001)]
chart[1]=[[1,1,1],[1,1,1],[1,1,1],[1]]

for i in range(2, 1001):
    for j in range(0, 10):
        now_row=j//3
        now_col=j%3
    
        d_r=[-1,1,0,0]
        d_c=[0,0,-1,1]
        ret=0
        for k in range(4):
            new_row=now_row+d_r[k]
            new_col=now_col+d_c[k]
            if movable(new_row, new_col):
                ret+=chart[i-1][new_row][new_col]
                ret%=MOD
        chart[i][now_row][now_col]=ret%MOD


for _ in range(T):
    n=int(sys.stdin.readline())
    
    one=sum(chart[n][0])
    two=sum(chart[n][1])
    three=sum(chart[n][2])
    four=sum(chart[n][3])
    print((one+two+three+four)%MOD)