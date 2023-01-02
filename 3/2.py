'''
위의 두수는 각각 row col 

1. 행 선택
2. 숫자 낮은 카드


입력
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
'''
import sys


N, M = map(int, sys.stdin.readline().rstrip().split())
# N 은 중요

arr = []

for i in range(0, N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

#print(arr)

arr = list(map(min, arr))

print(max(arr))
