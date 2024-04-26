N=int(input())

LIM=1000001

# 1부터 백만 사이의 소수를 구한다.
is_prime = [True for i in range(LIM)]

is_prime[0] = False
is_prime[1] = False
for i in range(2, LIM):
    if is_prime[i]:
        for j in range(i*2, LIM, i):
            is_prime[j] = False

# 일단 3분의 1을 잘 찾아봐야한다. 그리고 하나 늘리는거랑 하나 줄이는거랑 어떻게 하지?
'''
전 우주의 생명체 수를 현재의 절반으로 한다.
전 우주의 생명체 수를 현재의 1/3로 한다.
(위의 두 경우에서, 나누어 떨어지지 않으면 몫만 남기고, 나머지는 버린다.)
전 우주의 생명체 수를 현재보다 하나 늘린다.
전 우주의 생명체 수를 현재보다 하나 줄인다.
(이미 전 우주의 생명체 수가 0이라면 할 수 없다.)                         
'''

from collections import deque

def test(now, start, end):
    global is_prime
    
    visit=[False for i in range(LIM)]
    ans=LIM
    que = deque()
    que.append((now, 0))
    
    mul = [2, 3]
    pm = [1, -1]

    while que:
        num, depth = que.popleft()
        #print(num, depth)
        if(start<=num<=end and is_prime[num]):
            ans=min(depth, ans)

        for i in range(2):
            new_num = num // mul[i]
            
            if new_num < LIM and not visit[new_num]:
                visit[new_num] = True
                que.append((new_num, depth+1))
        for i in range(2):
            new_num = num + pm[i]
            if new_num < LIM and not visit[new_num]:
                visit[new_num] = True
                que.append((new_num, depth+1))


    if ans == LIM:
        ans=-1

    return ans


for i in range(N):
    now, start, end = map(int, input().split())
    start, end = (min(start, end), max(start, end))
    print(test(now, start, end))
