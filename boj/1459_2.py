row, col, one, cross = map(int, input().split())

# 대각선 시간을 구하기
# 대각선 갈꺼
mini=min(row, col)

# 그냥 갈꺼
left=max(row, col)-mini

if cross > one * 2:
    print((row+col)*one)
else:
    t=mini*cross
    other=0
    if cross < one:
        other+=left//2*2 * cross
        other+=(left%2) * one
    else:
        other+=left*one
    print(t+other)