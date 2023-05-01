# 2번 풀이 -> 라이브러리 이용

N, T = map(int, input().split())

li = list(map(int, input().split()))
# 7 2
# 1 1 2 2 2 2 3

# 7 4
# 1 1 2 2 2 2 3

from bisect import bisect_left, bisect_right

cnt = bisect_right(li, T) - bisect_left(li, T)

if not cnt:
    print(-1)
else:
    print(bisect_right(li, T) - bisect_left(li, T))

# 그냥 구현할꺼면 이전 이진탐색은 mid - 1 mid + 1이나 mid로 값을 설정하는 경우가 있다.

