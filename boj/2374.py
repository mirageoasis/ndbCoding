N=int(input())

chart = []

for i in range(N):
    chart.append(int(input()))

stack = [chart[0]]
maxi = chart[0]
cnt=0

# 올라 갈 때는 미리 더해준다는 느낌으로 더해주고
# 내려갈 때는 stack 을 교체만 하는 방식으로 한다.
# 마치고 stack에 잔류하고 있는 원소와 최대값의 차이를 더해주면 된다. 

for i in chart[1:]:
    if stack[0] > i:
        stack.pop()
        stack.append(i)
    elif stack[0] < i:
        cnt += (i - stack[-1])
        stack.pop()
        stack.append(i)
    else:
        pass
    maxi = max(maxi, i)

while stack:
    cnt += maxi - stack.pop()

print(cnt)