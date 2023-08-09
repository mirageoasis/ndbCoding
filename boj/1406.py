from collections import deque

string=input()
M=int(input())

left = deque()
right = deque()

for i in string:
    left.append(i)

# 명령어들 처리
for _ in range(M):
    li = input().strip().split()
    if li[0] == 'L':
        if len(left):
            tmp = left.pop()
            right.appendleft(tmp)
    elif li[0] == 'D':
        if len(right):
            tmp = right.popleft()
            left.append(tmp)
    elif li[0] == 'B':
        if len(left):
            tmp = left.pop()
    else:
        left.append(li[1])

while left:
    print(left.popleft(), end='')
while right:
    print(right.popleft(), end='')

print('')