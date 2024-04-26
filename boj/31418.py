import sys

W, H, K, T = map(int, input().split())

li = []
chart = []

for i in range(K):
    li.append(tuple(map(int, sys.stdin.readline().split())))


for i in li:
    wide, height = i
    
    wide_minus = min(wide - 1, T)
    wide_plus = min(W - wide, T)
    
    height_minus = min(height - 1, T)
    height_plus = min(H - height, T)
    #print(wide_minus, wide_plus, height_minus, height_plus)
    chart.append((wide_minus + wide_plus + 1) * (height_minus + height_plus + 1))

ans = 1
for c in chart:
    ans *= c
    ans %= 998244353

print(ans)