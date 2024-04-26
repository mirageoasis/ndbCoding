import sys

K=int(input())
N=int(input())
alpha = input()
# dict를 설정해서 (row col), (row, col) 이어져 있다고 얘기
graph = dict()
ladder = []
ans = ['x' for i in range(27)]

# 위 아래에서 왔다가 온 경우를 가정
# 둘이 비교를 해서 ????????를 해결, 이 때 이미 나온 수라면 즉시 값을 낸다.


# 여기의 idx는 ord를 적용해서 숫자를 추출한거다.
up_number = [-1 for i in range(K)]
down_number = [-1 for i in range(K)]
queston_line = 0

for i in range(N):
    ladder.append(list(sys.stdin.readline().strip()))
    if ladder[-1][0] == '?':
        queston_line = i

for i in ladder:
    print(i)

for i in range(N):
    for j in range(K - 1):
        if ladder[i][j] == '-':
            graph[(i, j + 1)] = (i, j)
            graph[(i, j)] = (i, j + 1)

# up
for i in range(K):
    #i 에 기록
    start_point = i
    for j in range(queston_line):
        if graph.get((j, start_point)) != None:
            row, col = graph.get((j, start_point))
            start_point = col

    up_number[i] = start_point


for idx ,i in enumerate(alpha):
    start_point = idx
    for j in range(N - 1, queston_line, -1):
        if graph.get((j, start_point)) != None:
            row, col = graph.get((j, start_point))
            start_point = col

    down_number[ord(i) - ord('A')] = start_point


print(up_number)
print(down_number)

for i in range(K):
    # 같은 경우
    # 차이가 2보다 큰 경우
    # 차이가 1인 경우

    # 이 때 아래의 라인이 이미 점거가 되어있다면 break print
    if up_number[i] == down_number[i]:
        # *
        if ans[up_number[i]] == '-':
            print('x' * (K - 1))
            break
        ans[up_number[i]] = '*'
    elif abs(up_number[i] - down_number[i]) == 1:
        # -
        if ans[min(up_number[i], down_number[i])] == '*':
            print('x' * (K - 1))
            break
        ans[min(up_number[i], down_number[i])] = '-'
    else:
        print('x' * (K - 1))
        break
else:
    real = []
    for i in ans[:K-1]:
        if i == 'x':
            real.append('*')
        else:
            real.append(i)

    ptr = ''.join(real)
    if '--' in ptr:
        print('x' * (K - 1))
    else:
        #print(''.join(ans))
        print(ptr)

'''
11
5
ABCEDJFKIHG
*-***-****
-*-******-
??????????
-**-***-*-
**-*-*-*-*
'''