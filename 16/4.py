N = int(input())
li = list(map(int, input().split()))
li.reverse()
li2 = []

# 1번 방법 -> n ^ 2
# for i in range(1, N):
#     for j in range(0, i):
#         if li[i] > li[j]:
#             li2[i] = max(li2[j] + 1, li2[i])

# print(N - max(li2))

# 2번 방법 -> n log n

# 0 1 2 3 4 5 6 7 8 9 10
# 
# 연속되어서 증가하는 수들 중에서 최소가 되는 값을 넣어준다.
from bisect import bisect_left

li2.append(li[0])
chart = [i for i in range(0, N+1)]

for i in range(1, N):
    if li[i] > li2[-1]:
        li2.append(li[i])
    else:
        idx = bisect_left(li2, li[i])
        li2[idx] = li[i]

print(N - len(li2))