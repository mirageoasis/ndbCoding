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
'''
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
'''

dx = [0, 0, -1, 1]
dy = [-1, 1, 0 , 0]
move_type = ['L', 'R', 'U', 'D']


for move in moves:
    newx, newy = 0 , 0
    for i in range(0, len(move_type)):
        if move_type[i] == move:
            newx = x + dx[i]
            newy = y + dy[i]
    if newx < 1 or newy < 1 or newx > N or newy > N:
        continue
    x, y = newx, newy
    

print(x, y)