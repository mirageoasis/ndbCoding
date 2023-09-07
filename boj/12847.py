import sys

N, M = map(int, input().split())

chart = list(map(int, sys.stdin.readline().split()))

# n 까지의 합 li 

# 슬라이딩 윈도우
maxi2 = sum([i for i in chart[:M]])
sums2 = sum([i for i in chart[:M]])

for i in range(M, N):
    sums2 += chart[i]
    sums2 -= chart[i - M]
    maxi2 = max(maxi2, sums2)

print(maxi2)

# 부분합

# li = [0]

# li[0] = chart[0]

# for i in chart[1:]:
#     li.append(li[-1] + i)

# #print(li)

# maxi = li[M - 1]

# for idx, i in enumerate(chart):
#     if idx > M - 1:
#         maxi = max(maxi, li[idx] - li[idx - M])


# print(maxi)