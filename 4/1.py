'''
지도 있다.
N -> 지도 크기
a b c d e -> 움직임
(0, 0)에서 시작해서 어디로 이동하는지 고르시오

5
R R R U D D
'''
import sys


N = int(input())
moves = sys.stdin.readline().rstrip().split()

x = 1
y = 1

for move in moves:
    if move == "R":
        y = min(N, y + 1)
    elif move == "L":
        y = max(1, y - 1)
    elif move == "D":
        x = min(N, x + 1)
    elif move == "U":
        x = max(1, x - 1)
    else:
        print("에러 발생")
    

print(x, y)