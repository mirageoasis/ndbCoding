
# 일단 커서에 삭제 추가가 되므로 array는 안됨
# linked list로 할 것인가?
# linked list도 좋지만 deque 2개를 활용하면 linked list같이 활용 가능함
from collections import deque
import sys

first_que=deque()
second_que=deque()

string=input()
n=int(input())
commands=[]

for i in range(n):
    commands.append(sys.stdin.readline().strip().split())

for i in string:
    first_que.append(i)

#print(first_que)

for command in commands:
    if command[0] == 'L':
        if first_que:
            second_que.appendleft(first_que.pop())
    elif command[0] == 'D':
        if second_que:
            first_que.append(second_que.popleft())
    elif command[0] == 'B':
        if first_que:
            first_que.pop()
    elif command[0] == 'P':
        first_que.append(command[1])

    #print(first_que, second_que)


fin=list(first_que+second_que)

print(''.join(fin))