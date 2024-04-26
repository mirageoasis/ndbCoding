import sys

N=int(input())

li = []
chart = [N][10001][2]

# 0번은 안쓴거, 1번은 쓴거

for i in range(N):
    li.append(list(map(int, sys.stdin.readline())))
li.sort(key=lambda x: (x[1]))


for money, day in range(len(li)):
    
    for d in day:
        pass
