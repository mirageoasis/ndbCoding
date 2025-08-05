# 오, 아

# 2가지 케이스만
# 5개면 그냥 완탐 ㄱ
# 10번이니까 2 ^ 10

# 30분 시작
n=int(input())

chart=[]

for i in range(n):
    chart.append(input().split())

nums = set()
nums.add('0')
nums.add('1')
nums.add('2')
nums.add('3')
nums.add('4')
nums.add('5')

from collections import deque
que=deque()
que.append([0, '+', 0, 0])

ans=[-(5**11), (5**11)]

while que:
    num, op, row, col = que.popleft()
    new_op='/'
    if op == '/':
        # 연산자와 추가하기
        new_op=chart[row][col]
    else:
        # 
        number=int(chart[row][col])
        if op == '+':
            num+=number
        elif op == '-':
            num-=number
        elif op == '*':
            num*=number
    if row == n - 1 and col == n - 1:
        ans[0] = max(ans[0], num)
        ans[1] = min(ans[1], num)
    d_r=[1, 0]
    d_c=[0, 1]
    for i in range(2):
        new_row = row + d_r[i]
        new_col = col + d_c[i]
        if 0 <= new_row < n and 0<=new_col < n:
            que.append([num, new_op, new_row, new_col])

print(*ans)