# 뒤로가기 
# 뒤로가기 공간 1개 이상
# 가장 최근에 접속, 그리고 삭제
# 현재 보고 있는거 앞으로 저장

# 앞으로 가기
# 현재보고 있는거 뒤로가기에 저장

# 그냥 접속
# 앞으로 삭제
# 현재 페이지 뒤로 추가

# 압축
# 뒤로가기 압축 실시


# 현재 페이지
# 큐 상태
import sys
input=sys.stdin.readline
kind, cnt = map(int, input().split())

# B 이후
# F 이전
# a 접속
# C 압축
from collections import deque
left=deque()
right=deque()
now=-1

for _ in range(cnt):
    i=input().strip()
    alpha=i[0]
    number=-1
    if len(i) > 1:
        number=int(i.split()[1]) 
    if alpha == 'B':
        if not left:
            #print(left, now, right)
            continue
        right.appendleft(now)
        now=left.pop()
    elif alpha == 'F':
        if not right:
            #print(left, now, right)
            continue
        left.append(now)
        now=right.popleft()
    elif alpha == 'C':
        if not left:
            #print(left, now, right)
            continue
        l=deque()
        l.append(left.popleft())
        while left:
            poped=left.popleft()
            if l[-1] != poped:
                l.append(poped)
        left=l
    elif alpha == 'A':
        if now != -1:
            left.append(now)
        right=deque()
        now=number
    #print(left, now, right)

#print(left, now, right)
left=list(left)
right=list(right)
#print(left, now, right)
print(now)
print(*(list(reversed(left)) if left else [-1]))
print(*(right if right else [-1]))